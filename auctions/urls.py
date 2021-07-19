from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.index_view, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("categories/", views.categories_view, name="categories"),
    path("category/<str:category>/", views.category_view, name="category"),
    path("create/", views.create_view, name="create"),
    path("submit/", views.submit_view, name="submit"),
    path("listings/<int:id>", views.listings_view, name="listings"),
    path("submit-bid/<int:listingid>", views.submit_bid_view, name="submit-bid"),
    path("submit-comment/<int:listingid>", views.submit_comment_view, name="comment"),
    path("add-watchlist/<int:listingid>", views.add_watchlist_view, name="add-watchlist"),
    path("remove-watchlist/<int:listingid>", views.remove_watchlist_view, name="remove-watchlist"),
    path("watchlist/<str:username>", views.watchlist_view, name="watchlist"),
    path("close-bid/<int:listingid>", views.close_bid_view, name="close-bid"),
    path("my-winnings", views.my_winnings_view, name="my-winnings")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
