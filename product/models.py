from django.db import models
from django.contrib.auth.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductGroup(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    age_limit = models.CharField(max_length=999, blank=True)
    price = models.FloatField()
    on_sale = models.BooleanField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.CharField(max_length=999)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.image


class ReviewedItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product.id)
