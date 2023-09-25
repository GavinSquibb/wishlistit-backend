from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *
from wishlistit.serializers import *


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class WishListListView(generics.ListAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer


class WishListCreateView(generics.ListCreateAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer


class WishListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer


class GiftItemListCreateView(generics.ListCreateAPIView):
    queryset = GiftItem.objects.all()
    serializer_class = GiftItemSerializer


class GiftItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GiftItem.objects.all()
    serializer_class = GiftItemSerializer


class GiftItemsByWishListView(generics.ListAPIView):
    serializer_class = GiftItemSerializer

    def get_queryset(self):
        # Get the `WishList` ID from the URL parameters
        wishlist_id = self.kwargs["wishlist_id"]

        # Filter `GiftItem` objects based on the `WishList` ID
        queryset = GiftItem.objects.filter(wish_list=wishlist_id)

        return queryset
