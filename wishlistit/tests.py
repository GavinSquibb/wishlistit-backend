from django.contrib.auth.models import User, Group
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from .models import WishList, GiftItem
from .serializers import WishListSerializer, GiftItemSerializer


class LogoutViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token.access_token}")

    def test_logout_success(self):
        url = reverse("logout")
        data = {"refresh_token": str(self.token)}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)


class WishListViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)
        self.wishlist = WishList.objects.create(
            name="Test Wishlist",
            creator=self.user,
        )

    def test_list_wishlists(self):
        url = reverse("wishlist-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GiftItemCreateViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)
        self.wishlist = WishList.objects.create(
            name="Test Wishlist",
            creator=self.user,
        )

    def test_create_gift_item(self):
        url = reverse("giftitem-list-create")
        data = {
            "name": "Test Gift Item",
            "description": "Description of the test gift item",
            "price": "25.99",
            "purchased": False,
            "wish_list": self.wishlist.wish_list_id,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class GiftItemDetailViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.force_authenticate(user=self.user)
        self.wishlist = WishList.objects.create(
            name="Test Wishlist",
            creator=self.user,
        )
        self.gift_item = GiftItem.objects.create(
            name="Test Gift Item",
            price="25.99",
            purchased=False,
            wish_list=self.wishlist,
        )

    def test_retrieve_gift_item(self):
        url = reverse("giftitem-detail", args=[self.gift_item.gift_item_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_gift_item(self):
        url = reverse("giftitem-detail", args=[self.gift_item.gift_item_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
