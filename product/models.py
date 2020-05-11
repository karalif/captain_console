from django.db import models

#class GameCategory(models.Model):
#    name = models.CharField(max_length=255)

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
    age_limit = models.CharField(max_length=999)
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