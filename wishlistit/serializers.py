from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class GiftItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftItem
        fields = "__all__"


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id", "username", "content", "timestamp")
        read_only_fields = ("id", "timestamp")
