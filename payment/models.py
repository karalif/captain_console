from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class BillingInfo(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    active = models.BooleanField(default=True)


class PaymentInfo(models.Model):
    full_name = models.CharField(max_length=255)
    card_number = models.DecimalField(max_digits=19, decimal_places=0)
    exp_month = models.DecimalField(max_digits=2, decimal_places=0)
    exp_year = models.DecimalField(max_digits=2, decimal_places=0)
    cvv = models.DecimalField(max_digits=3, decimal_places=0)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    active = models.BooleanField(default=True)


class Order(models.Model):
    ordered_products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=2, decimal_places=0)
    billing_info = models.ForeignKey(BillingInfo, null=True, on_delete=models.DO_NOTHING)
    payment_info = models.ForeignKey(PaymentInfo, null=True, on_delete=models.DO_NOTHING)
    step = models.CharField(max_length=255, default="billing")

    def __str__(self):
        return self.user


