from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Cart

@login_required()
def my_cart(request):
    if request.method == 'GET':
        prod = []
        for x in Cart.objects.filter(user_id = request.user.id):
            prod.append(str(x))
        prod_int = [int(i) for i in prod]
        context = {'items': Product.objects.filter(id__in = prod_int), 'totalprice': _total_price(prod_int)}
        return render(request,'shopping_cart/my_cart.html', context)


@login_required()
def add_to_cart(request, id):
    prod = []
    for x in Cart.objects.filter(user_id=request.user.id):
        prod.append(str(x))
    prod_int = [int(i) for i in prod]
    if id in prod_int:
        updated_quantity = Cart.objects.get(product_id = id).quantaty + 1
        cartitem = Cart(user_id=request.user.id, product_id=id, quantity=updated_quantity)
        cartitem.save()
        print()
    else:
        cartitem = Cart(user_id=request.user.id, product_id=id, quantity=1)
        cartitem.save()
        print()
    return render(request, 'product/product_details.html', {
            'product': get_object_or_404(Product, pk=id)
    })

def _total_price(prodid_list):
    totalPrice = 0
    for i in prodid_list:
        totalPrice += Product.objects.get(id=i).price
    return totalPrice

@login_required()
def delete_from_cart(request, id):
    for x in Cart.objects.filter(user_id=request.user.id):
        if str(x) == str(id):
            product = get_object_or_404(Cart, pk=x.id)
            product.delete()

    return my_cart(request)

