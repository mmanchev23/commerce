from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import datetime


# Done
def index_view(request):
    listings = Listing.objects.all()
    context = {}

    try:
        watchlist = Watchlist.objects.filter(user=request.user.username)
        watchlist_count = len(watchlist)
    except:
        watchlist_count = None

    context = {
        "listings": listings,
        "watchlist_count": watchlist_count
    }

    return render(request, "auctions/index.html", context)


# Done
def register_view(request):
    context = {}

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
        return render(request, "auctions/register.html")


# Done
def login_view(request):
    context = {}

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


# Done
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


# Done
def categories_view(request):
    listings = Listing.objects.raw("SELECT * FROM auctions_listing GROUP BY category")
    context = {}

    try:
        watchlists = Watchlist.objects.filter(user=request.user.username)
        watchlists_count = len(watchlists)
    except:
        watchlists_count = None

    context = {
        "listings": listings,
        "watchlists_count": watchlists_count
    }

    return render(request, "auctions/categories.html", context)


# Done
def category_view(request, category):
    category_items = Listing.objects.filter(category=category)
    context = {}

    try:
        watchlists = Watchlist.objects.filter(user=request.user.username)
        watchlists_count = len(watchlists)
    except:
        watchlists_count = None

    context = {
        "category_items": category_items,
        "category": category,
        "watchlists_count": watchlists_count
    }

    return render(request,"auctions/category.html", context)


# Done
def create_view(request):
    context = {}

    try:
        watchlists = Watchlist.objects.filter(user=request.user.username)
        watchlists_count = len(watchlists)
    except:
        watchlists_count = None

    context = {
        "watchlists_count": watchlists_count
    }

    return render(request,"auctions/create.html", context)


# Done
def submit_view(request):
    if request.method == "POST":
        listing = Listing()
        listing.user = request.user.username
        listing.title = request.POST['title']
        listing.description = request.POST['description']
        listing.price = request.POST['price']
        listing.category = request.POST['category']

        if request.POST['image']:
            listing.image = request.POST['image']

        listing.save()

        all_listing = AllListing()
        items = Listing.objects.all()
        for item in items:
            try:
                if AllListing.objects.get(id=item.id):
                    pass
            except:
                all_listing.title = item.title
                all_listing.description = item.description
                all_listing.image = item.image
                all_listing.save()

        return redirect('index')
    else:
        return redirect('index')


# Done
def listings_view(request, id):
    context = {}

    try:
        listing = Listing.objects.get(id=id)
    except:
        return redirect('index')

    try:
        comments = Comment.objects.filter(listing=id)
    except:
        comments = None

    if request.user.username:
        try:
            if Watchlist.objects.get(user=request.user.username, listing=listing):
                added=True
        except:
            added = False

        try:
            listing = Listing.objects.get(id=id)
            if listing.owner == request.user.username:
                owner=True
            else:
                owner=False
        except:
            return redirect('index')
    else:
        added=False
        owner=False

    try:
        watchlist = Watchlist.objects.filter(user=request.user.username)
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


# Done
def submit_bid_view(request, id):
    current_bid = Listing.objects.get(id=id)
    current_bid = current_bid.price

    if request.method == "POST":
        user_bid = request.POST["bid"]

        if user_bid > current_bid:
            listing_items = Listing.objects.get(id=id)
            listing_items.price = user_bid
            listing_items.save()

            try:
                if Bid.objects.filter(id=id):
                    bidrow = Bid.objects.filter(id=id)
                    bidrow.delete()

                bidtable=Bid()
                bidtable.user=request.user.username
                bidtable.title=listing_items.title
                bidtable.bid = user_bid
                bidtable.save()
                
            except:
                bidtable = Bid()
                bidtable.user=request.user.username
                bidtable.title = listing_items.title
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

# Done
def submit_comment_view(request, listing):
    if request.method == "POST":
        comment = Comment()

        comment.listing = listing
        comment.user = request.user.username
        comment.comment = request.POST['comment']

        comment.save()
        return redirect('listings', id=listing)
    else :
        return redirect('index')

# Done
def add_watchlist_view(request, id):
    listing = Listing.objects.get(id=id)

    if request.user.username:
        watchlist = Watchlist()
        watchlist.user = request.user.username
        watchlist.listing = listing
        watchlist.save()
        return redirect('listings', id=id)
    else:
        return redirect('index')
