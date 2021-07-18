from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import datetime


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


def register_view(request):
    context = {}

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            context = {
                "message": "Passwords must match."
            }

            return render(request, "auctions/register.html", context)

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            context = {
                "message": "Username already taken."
            }

            return render(request, "auctions/register.html", context)

        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


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


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


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
