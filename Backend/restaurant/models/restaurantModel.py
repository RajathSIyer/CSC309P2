from django.db import models
from django.db.models import SET_NULL
from django.conf import settings


class restaurant(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=30, null=False, blank=False)
    postalCode = models.CharField(max_length=30, null=False, blank=False)
    phoneNumber = models.CharField(max_length=30, null=False, blank=False)
    logo = models.ImageField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    class RestaurantTypes(models.TextChoices):
        FRESHMAN = 'IN', _('Indian')
        SOPHOMORE = 'IT', _('Italian')
        JUNIOR = 'AM', _('American')
        SENIOR = 'PI', _('Pizza')
        GRADUATE = 'CH', _('Chinese')
    type = models.CharField(max_length=8, choices=RestaurantTypes)