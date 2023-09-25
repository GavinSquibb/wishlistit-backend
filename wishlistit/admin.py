from django.contrib import admin
from .models import WishList, GiftItem, Discussion, Comment

admin.site.register(WishList)
admin.site.register(GiftItem)
admin.site.register(Discussion)
admin.site.register(Comment)
