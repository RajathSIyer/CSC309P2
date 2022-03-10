from django.db import models
from django.db.models import SET_NULL
ReactionChoice = (('Like', 'LIKE'), ('Dislike', 'DISLIKE'))

class comment(models.Model):
    title = models.CharField()
    context = models.CharField()
    owner = models.ForeignKey(to=Owner,null=False) #related name, onDelete??
    restaurant = models.ForeignKey(to=restaurant,null=False)


