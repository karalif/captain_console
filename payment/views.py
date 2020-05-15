from django.shortcuts import render, redirect, get_object_or_404
from shopping_cart.models import Cart
from product.models import Product
from django.contrib.auth.decorators import login_required
from shopping_cart.views import _total_price
from payment.models import Order


def billing_info(request):
    prod = []
    item_count = 0
    for x in Cart.objects.filter(user_id=request.user.id):
        prod.append(str(x))
        item_count += 1
    prod_int = [int(i) for i in prod]
    context = {'items': Product.objects.filter(id__in=prod_int), 'totalprice': _total_price(prod_int, request.user.id),
               'itemcount': item_count}
    return render(request, 'payment/billing_address.html', context)


def payment_info(request):
    prod = []
    item_count = 0
    for x in Cart.objects.filter(user_id=request.user.id):
        prod.append(str(x))
        item_count += 1
    prod_int = [int(i) for i in prod]
    context = {'items': Product.objects.filter(id__in=prod_int), 'totalprice': _total_price(prod_int, request.user.id),
               'itemcount': item_count}
    return render(request, 'payment/payment_info.html', context)


def order_overview(request):
    prod = []
    item_count = 0
    for x in Cart.objects.filter(user_id=request.user.id):
        prod.append(str(x))
        item_count += 1
    prod_int = [int(i) for i in prod]
    context = {'items': Product.objects.filter(id__in=prod_int), 'totalprice': _total_price(prod_int, request.user.id),
               'itemcount': item_count}
    return render(request, 'payment/overview.html', context)


def confirmation(request):
    prod = []
    item_count = 0
    for x in Cart.objects.filter(user_id=request.user.id):
        prod.append(str(x))
        item_count += 1

    prod_int = [int(i) for i in prod]
    create_order = Order.objects.create(user_id=request.user.id, quantity=item_count)

    for x in Product.objects.filter(id__in=prod_int):
        create_order.ordered_products.add(x)

    context = {'items': Product.objects.filter(id__in=prod_int),
               'totalprice': _total_price(prod_int, request.user.id),
               'itemcount': item_count}

    delete_cart(request)
    return render(request, 'payment/confirmation.html', context)


def delete_cart(request):
    for x in Cart.objects.filter(user_id=request.user.id):
        product = get_object_or_404(Cart, pk=x.id)
        product.delete()
