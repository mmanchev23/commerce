from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import datetime


context = {}

def index_view(request):
    try:
        listings = Listing.objects.all()
        user = User.objects.get(username=request.user.username)
        watchlists = Watchlist.objects.filter(user=user)
        watchlist_count = len(watchlists)
    except:
        listings = None
        user = None
        watchlists = None
        watchlist_count = None

    context = {
        "listings": listings,
        "watchlist_count": watchlist_count
    }

    return render(request, "auctions/index.html", context)

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            context = {
                "message": "Passwords must match!"
            }

            return render(request, "auctions/register.html", context)

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            context = {
                "message": "Username already taken!"
            }

            return render(request, "auctions/register.html", context)

        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html", context)

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            context = {
                "message": "Invalid username and/or password."
            }

            return render(request, "auctions/login.html", context)
    else:
        return render(request, "auctions/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def categories_view(request):
    try:
        listings = Listing.objects.raw("SELECT * FROM auctions_listing GROUP BY category")
        user = User.objects.get(username=request.user.username)
        watchlists = Watchlist.objects.filter(user=user)
        watchlists_count = len(watchlists)
    except:
        listings = None
        user = None
        watchlists = None
        watchlists_count = None

    context = {
        "listings": listings,
        "watchlists_count": watchlists_count
    }

    return render(request, "auctions/categories.html", context)

def category_view(request, category):
    try:
        category_items = Listing.objects.filter(category=category)
        user = User.objects.get(username=request.user.username)
        watchlists = Watchlist.objects.filter(user=user)
        watchlists_count = len(watchlists)
    except:
        category_items = None
        user = None
        watchlists = None
        watchlists_count = None

    context = {
        "category_items": category_items,
        "category": category,
        "watchlists_count": watchlists_count
    }

    return render(request, "auctions/category.html", context)

def create_view(request):
    try:
        user = User.objects.get(username=request.user.username)
        watchlists = Watchlist.objects.filter(user=user)
        watchlists_count = len(watchlists)
    except:
        user = None
        watchlists = None
        watchlists_count = None

    context = {
        "watchlists_count": watchlists_count
    }

    return render(request, "auctions/create.html", context)

def submit_view(request):
    if request.method == "POST":
        try:
            user = User.objects.get(username=request.user.username)
        except:
            user = None

        listing = Listing()
        listing.user = user
        listing.title = request.POST['title']
        listing.description = request.POST['description']
        listing.price = request.POST['price']
        listing.category = request.POST['category']
        listing.image = request.POST['image']
        listing.save()

        all_listing = AllListing()
        items = Listing.objects.all()
        for item in items:
            try:
                if AllListing.objects.get(listing=item):
                    pass
            except:
                all_listing.title = item.title
                all_listing.description = item.description
                all_listing.save()

        return redirect('index')
    else:
        return redirect('index')

def listings_view(request, id):
    try:
        user = User.objects.get(username=request.user.username)
        listing = Listing.objects.get(id=id)
        comments = Comment.objects.filter(listing=listing)
    except:
        user = None
        listing = None
        comments = None
        return redirect('index')

    if request.user.username:
        try:
            if Watchlist.objects.get(user=user, listing=listing):
                added=True
        except:
            added = False

        try:
            listing = Listing.objects.get(id=id)
            if listing.user == user:
                owner=True
            else:
                owner=False
        except:
            return redirect('index')
    else:
        added=False
        owner=False

    try:
        watchlist = Watchlist.objects.filter(user=user)
        watchlist_count=len(watchlist)
    except:
        watchlist_count=None

    context = {
        "listing": listing,
        "error": request.COOKIES.get('error'),
        "errorgreen": request.COOKIES.get('errorgreen'),
        "comments": comments,
        "added": added,
        "owner": owner,
        "watchlist_count": watchlist_count
    }

    return render(request, "auctions/listings.html", context)

def submit_bid_view(request, id):
    try:
        user = User.objects.get(username=request.user.username)
        current_bid = Listing.objects.get(id=id)
        current_bid = current_bid.price
    except:
        user = None
        current_bid = None

    if request.method == "POST":
        user_bid = request.POST["bid"]

        if Decimal(user_bid) > current_bid:
            listing_items = Listing.objects.get(id=id)
            listing_items.price = user_bid
            listing_items.save()

            try:
                if Bid.objects.filter(id=id):
                    bidrow = Bid.objects.filter(id=id)
                    bidrow.delete()

                bidtable = Bid()
                bidtable.user = user
                bidtable.title = listing_items.title
                bidtable.bid = user_bid
                bidtable.save()
                
            except:
                bidtable = Bid()
                bidtable.user = user
                bidtable.title =  listing_items.title
                bidtable.bid = user_bid
                bidtable.save()

            response = redirect('listings', id=id)
            response.set_cookie('errorgreen', 'Bid successfull!', max_age=3)
            return response
        else :
            response = redirect('listings',id=id)
            response.set_cookie('error', 'Bid should be greater than current price!', max_age=3)
            return response
    else:
        return redirect('index')

def submit_comment_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        user = User.objects.get(username=request.user.username)
    except:
        listing = None
        user = None

    if request.method == "POST":
        comment = Comment()

        comment.listing = listing
        comment.user = user
        comment.comment = request.POST['comment']

        comment.save()
        return redirect('listings', id=id)
    else :
        return redirect('index')

def add_watchlist_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        user = User.objects.get(username=request.user.username)
    except:
        listing = None
        user = None

    if request.user.username:
        watchlist = Watchlist()
        watchlist.user = user
        watchlist.listing = listing
        watchlist.save()
        return redirect('listings', id=id)
    else:
        return redirect('index')

def remove_watchlist_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        user = User.objects.get(username=request.user.username)
    except:
        listing = None
        user = None

    if request.user.username:
        try:
            watchlist = Watchlist.objects.get(user=user, listing=listing)
            watchlist.delete()
            return redirect('listings', id=id)
        except:
            return redirect('listings', id=id)
    else:
        return redirect('index')

def watchlist_view(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        user = None

    if request.user.username:
        try:
            watchlist = Watchlist.objects.filter(user=user)
            items = []

            for item in watchlist:
                items.append(Listing.objects.filter(title=item.listing))
            try:
                watchlist = Watchlist.objects.filter(user=user)
                watchlist_count = len(watchlist)
            except:
                watchlist_count=None

            context = {
                "items": items,
                "watchlist_count": watchlist_count
            }

            return render(request,"auctions/watchlist.html", context)
        except:
            try:
                watchlist = Watchlist.objects.filter(user=user)
                watchlist_count = len(watchlist)
            except:
                watchlist_count = None

            context = {
                "items": None,
                "watchlist_count": watchlist_count
            }
            return render(request, "auctions/watchlist.html", context)
    else:
        return redirect('index')

def close_bid_view(request, id):
    if request.user.username:
        try:
            listing = Listing.objects.get(id=id)
            user = User.objects.get(username=request.user.username)
        except:
            listing = None
            user = None
            return redirect('index')
            
        try:
            closed_bid = ClosedBid()
            title = listing.title
            closed_bid.user = listing.user
        except:
            closed_bid = None
            title = None
            close_bid.user = None

        try:
            bidrow = Bid.objects.get(listing=listing, bid=listing.price)
            closed_bid.winner = bidrow.user.username
            closed_bid.winprice = bidrow.bid
            closed_bid.save()
            bidrow.delete()
        except:
            closed_bid.winner = listing.user
            closed_bid.winprice = listing.price
            closed_bid.save()

        try:
            if Watchlist.objects.filter(listing=listing):
                watchrow = Watchlist.objects.filter(listing=listing)
                watchrow.delete()
            else:
                pass
        except:
            pass

        try:
            crow = Comment.objects.filter(listing=listing)
            crow.delete()
        except:
            pass

        try:
            brow = Bid.objects.filter(listing=listing)
            brow.delete()
        except:
            pass

        try:
            closed_bid_list = ClosedBid.objects.filter(listing=listing)
        except:
            closed_bid.user = listing.user
            closed_bid.winner = listing.user
            closed_bid.winprice = listing.price
            closed_bid.save()
            closed_bid_list = ClosedBid.objects.filter(listing=listing)

        listing.delete()

        try:
            watchlist = Watchlist.objects.filter(user=user)
            watchlist_count = len(watchlist)
        except:
            watchlist_count = None

        context = {
            "closed_bid_list": closed_bid_list,
            "title": title,
            "watchlist_count": watchlist_count
        }

        return render(request, "auctions/winningpage.html", context)   

    else:
        return redirect('index')

def my_winnings_view(request):
    if request.user.username:
        items = []

        try:
            user = User.objects.get(username=request.user.username)
            won_items = ClosedBid.objects.filter(winner=user)
            for won_item in won_items:
                items.append(AllListing.objects.filter(listing=won_item.listing))
        except:
            user = None
            won_items = None
            items = None
        try:
            watchlist = Watchlist.objects.filter(user=user)
            watchlist_count=len(watchlist)
        except:
            watchlist_count=None

        context = {
            "items": items,
            "watchlist_count": watchlist_count,
            "won_items": won_items
        }

        return render(request, 'auctions/winnings.html', context)
    else:
        return redirect('index')
