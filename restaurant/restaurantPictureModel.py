from django.db import models
from django.db.models import SET_NULL

class restaurantPicture(models.Model):
    alt_code = models.CharField(max_length=20, blank=True, null=True)
    restaurant = models.ForeignKey(to=restaurant)
    image = models.ImageField()