from django.urls import path
from . import views

urlpatterns = [
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("wishlists/", views.WishListListView.as_view(), name="wishlist-list"),
    path("wishlist/create", views.WishListCreateView.as_view(), name="wishlist-create"),
    path(
        "wishlist/<int:pk>", views.WishListDetailView.as_view(), name="wishlist-detail"
    ),
    path(
        "giftitems/",
        views.GiftItemListCreateView.as_view(),
        name="giftitem-list-create",
    ),
    path(
        "giftitems/<int:pk>/",
        views.GiftItemRetrieveUpdateDestroyView.as_view(),
        name="giftitem-detail",
    ),
    path(
        "giftitems/wishlist/<int:wishlist_id>/",
        views.GiftItemsByWishListView.as_view(),
        name="giftitems-by-wishlist",
    ),
]
