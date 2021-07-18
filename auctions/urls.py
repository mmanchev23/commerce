from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("categories/", views.categories_view, name="categories"),
    path("category/<str:category>/", views.category_view, name="category"),
    path("create/", views.create_view, name="create"),
    path("submit/", views.submit_view, name="submit"),
    path("listings/<int:id>/", views.listings_view, name="listings"),
    path("bid/submit/<int:listing-id>/", views.submit_bid_view, name="submit-bid"),
    path("comment/submit/<int:listingid>/", views.submit_comment_view, name="submit-comment"),
    path("watchlist/add/<int:listingid>/", views.add_watchlist_view, name="add-watchlist"),
    path("watchlist/remove/<int:listingid>/", views.remove_watchlist_view, name="remove-watchlist"),
    path("watchlist/<str:username>/", views.watchlist_view, name="watchlist"),
    path("closebid/<int:listingid>/", views.close_bid_view, name="close-bid"),
    path("my-winnings/", views.my_winnings_view, name="my-winnings")
]
