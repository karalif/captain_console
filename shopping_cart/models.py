from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=2, decimal_places = 0)
    def __str__(self):
        return str(self.product.id)