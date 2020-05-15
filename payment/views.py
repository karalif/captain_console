from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import HttpResponseNotFound
from shopping_cart.models import Cart
from product.models import Product
from django.contrib.auth.decorators import login_required
from shopping_cart.views import _total_price
from payment.models import Order, BillingInfo, PaymentInfo
from payment.forms.payment_form import PaymentBillingForm, PaymentInfoForm


def payment_info(request):
    b_info = BillingInfo.objects.filter(user_id=request.user.id, active=True)
    if len(b_info) == 0:
        return render(request, '404.html')
    p_info = PaymentInfo.objects.filter(user_id=request.user.id, active=True)
    for p in p_info:
        p.active = False
        p.save()
    if request.method == 'POST':
        form = PaymentInfoForm(data=request.POST)
        if form.is_valid():
            p_info = form.save()
            p_info.user_id = request.user.id
            p_info.active = True
            p_info.save()
            return redirect('/payment/overview')
    else:
        form = PaymentInfoForm(data=request.GET)
    return render(request, 'payment/payment_submit.html', {
        'form': form
    })


def billing_info(request):
    cart = Cart.objects.filter(user_id = request.user.id)
    if len(cart) == 0:
        return render(request, '404.html')
    b_info = BillingInfo.objects.filter(user_id=request.user.id, active=True)
    for b in b_info:
        b.active = False
        b.save()
    if request.method == 'POST':
        form = PaymentBillingForm(data=request.POST)
        if form.is_valid():
            billing_info = form.save()
            billing_info.user_id = request.user.id
            billing_info.active = True
            billing_info.save()
            return redirect('/payment/payment_info')
    else:
        form = PaymentBillingForm(data=request.GET)
    return render(request, 'payment/billing_submit.html', {
        'form': form
    })


def order_overview(request):
    prod = []
    item_count = 0
    p_info = PaymentInfo.objects.filter(user_id=request.user.id, active=True)
    if len(p_info) == 0:
        return render(request, '404.html')

    if request.method == "POST":
        return create_order(request)

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
    try:
        b_info = BillingInfo.objects.get(user_id=request.user.id, active=True)
        p_info = PaymentInfo.objects.get(user_id=request.user.id, active=True)
        _ = Order.objects.get(user_id=request.user.id, billing_info=b_info, payment_info=p_info)
    except Exception as e:
        print(e)
        return render(request, '404.html')

    b_info.active = False
    b_info.save()

    p_info.active = False
    p_info.save()

    for x in Cart.objects.filter(user_id=request.user.id):
        prod.append(str(x))
        item_count += 1

    prod_int = [int(i) for i in prod]

    context = {'items': Product.objects.filter(id__in=prod_int),
               'totalprice': _total_price(prod_int, request.user.id),
               'itemcount': item_count}

    delete_cart(request)
    return render(request, 'payment/confirmation.html', context)


def delete_cart(request):
    for x in Cart.objects.filter(user_id=request.user.id):
        product = get_object_or_404(Cart, pk=x.id)
        product.delete()


def create_order(request):
    prod = []
    item_count = 0
    for x in Cart.objects.filter(user_id=request.user.id):
        prod.append(str(x))
        item_count += 1
    try:
        b_info = BillingInfo.objects.get(user_id=request.user.id, active=True)
        p_info = PaymentInfo.objects.get(user_id=request.user.id, active=True)
    except:
        return render(request, '404.html')
    prod_int = [int(i) for i in prod]

    create_order = Order.objects.create(user_id=request.user.id, quantity=item_count, billing_info=b_info, payment_info=p_info)

    for x in Product.objects.filter(id__in=prod_int):
        create_order.ordered_products.add(x)

    return HttpResponse('')
