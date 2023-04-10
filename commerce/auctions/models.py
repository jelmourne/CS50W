from django.contrib.auth.models import AbstractUser
from django.db import models

"""
1.Your application should have at least three models in 
addition to the User model: one for auction listings, one 
for bids, and one for comments made on auction listings.
It's up to you to decide what fields each model should have, 
and what the types of those fields should be. You may have 
additional models if you would like.
"""

class User(AbstractUser):
    def __self__(self):
        return f"{self.username}"

class auction_listing(models.Model):
    auction_user = models.OneToOneField("User", verbose_name=("user"), on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    desciption = models.TextField()
    bid = models.OneToOneField("auction_bid", verbose_name=("bids"), on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    image = models.ImageField()

    
class action_watchlist():
    pass

class auction_bid(models.Model):
    bid = models.PositiveIntegerField()

class auction_comment(models.Model):
    pass