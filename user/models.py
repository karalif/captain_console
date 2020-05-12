from django.db import models
from django.contrib.auth.models import User
from product.models import Product
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=99,blank=True)
    birth_date = models.DateField(default=datetime.date.today)
    address = models.CharField(max_length=999,blank=True)
    zip_code = models.CharField(max_length=999,blank=True)
    city = models.CharField(max_length=999,blank=True)
    country = models.CharField(max_length=999,blank=True)
    profile_image = models.CharField(max_length=9999,blank=True)