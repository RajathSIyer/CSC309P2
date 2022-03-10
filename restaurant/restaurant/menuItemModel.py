from django.db import models
from django.db.models import SET_NULL

class menuItem(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    description = models.CharField(max_length=30, null=False, blank=False)
    price = models.DecimalField(decimal_places=2, null=False, blank=False)
    menu_category = models.ForeignKey(to=menuCategory)