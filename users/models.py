from django.contrib.auth.models import User
from django.db import models
from products.models import Product


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    house_number = models.IntegerField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=50)
    telephone_number = models.IntegerField()
    email = models.CharField(max_length=50, null=True)
    is_subscribed = models.BooleanField(default=False)
    profile_picture = models.CharField(max_length=9999)