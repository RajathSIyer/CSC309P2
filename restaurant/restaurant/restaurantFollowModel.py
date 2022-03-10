from django.db import models
from django.db.models import SET_NULL
ReactionChoice = (('Like', 'LIKE'), ('Dislike', 'DISLIKE'))

class restaurantFollow(models.Model):
    type = models.CharField(max_length=7, choices=ReactionChoice)
    restaurant = models.ForeignKey(to=RestaurantModel, null=False, blank=False)
    owner = models.ForeignKey(to=Owner,null=False) #related name, onDelete??

