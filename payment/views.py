from django.shortcuts import render, redirect
from shopping_cart.models import Cart
from product.models import Product
from django.contrib.auth.decorators import login_required
from shopping_cart.views import _total_price

def billing_info(request):
    prod = []
    item_count = 0
    for x in Cart.objects.filter(user_id=request.user.id):
        prod.append(str(x))
        item_count += 1
    prod_int = [int(i) for i in prod]
    context = {'items': Product.objects.filter(id__in=prod_int), 'totalprice': _total_price(prod_int),
               'itemcount': item_count}
    return render(request, 'payment/billing_address.html', context)

def payment_info(request):
    prod = []
    item_count = 0
    for x in Cart.objects.filter(user_id=request.user.id):
        prod.append(str(x))
        item_count += 1
    prod_int = [int(i) for i in prod]
    context = {'items': Product.objects.filter(id__in=prod_int), 'totalprice': _total_price(prod_int),
               'itemcount': item_count}
    return render(request, 'payment/payment_info.html', context)
