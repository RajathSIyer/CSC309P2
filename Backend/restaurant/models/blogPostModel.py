from django.db import models
from django.db.models import SET_NULL

class blogPost(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False)
    short_description = models.CharField(max_length=50, null=False, blank=False)
    restaurant = models.ForeignKey(to=restaurant)
    content = models.CharField()
    like_count = models.PositiveBigIntegerField()
    dislike_count = models.PositiveBigIntegerField()
