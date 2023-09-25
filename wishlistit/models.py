from django.db import models


class Discussion(models.Model):
    discussion_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    discussion = models.ForeignKey(
        Discussion, related_name="comments", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class WishList(models.Model):
    wish_list_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        "auth.User", related_name="wish_lists", on_delete=models.CASCADE
    )
    invited_users = models.ManyToManyField(
        "auth.user", related_name="invited_wishlists", blank=True, null=True
    )
    discussion = models.ForeignKey(
        Discussion, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.name


class GiftItem(models.Model):
    gift_item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchased = models.BooleanField(default=False)
    link = models.CharField(max_length=200, blank=True, null=True)
    wish_list = models.ForeignKey(
        WishList, related_name="gift_items", on_delete=models.CASCADE
    )
    discussion = models.ForeignKey(
        Discussion, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.name


class Message(models.Model):
    username = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "chat_message"
        ordering = ("timestamp",)
