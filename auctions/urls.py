from django.urls import path
from . import views
from django.templatetags.static import static
from commerce import settings


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
    path("submit-bid/<int:id>", views.submit_bid_view, name="submit-bid"),
    path("submit-comment/<int:id>", views.submit_comment_view, name="comment"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
