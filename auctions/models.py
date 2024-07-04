from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionListing(models.Model):
    items = models.CharField(max_length=64)
    description = models.CharField(max_length=450)
    bid = models.IntegerField()
    img = models.URLField(blank=True)
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.items}"

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.user} commented: {self.content}"
    
class Bids(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.bid} has made a bid of R {self.bid}"