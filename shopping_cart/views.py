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
            prod.append(x)
        print(prod)
        prod_ids = [p.product_id for p in prod]
        context = {'items': prod, 'totalprice': _total_price(prod_ids, request.user.id)}
        return render(request,'shopping_cart/my_cart.html', context)

@login_required()
def add_to_cart(request, id):
    prod = []
    for x in Cart.objects.filter(user_id=request.user.id):
        prod.append(str(x))
    prod_int = [int(i) for i in prod]
    if id in prod_int and id == Cart.objects.get(user_id = request.user.id, product_id = id).product_id:
        cartitem = Cart.objects.get(user_id = request.user.id, product_id = id)
        cartitem.quantity += 1
    else:
        cartitem = Cart(user_id=request.user.id, product_id=id, quantity=1)
    cartitem.save()
    print()
    return redirect('/products/' + str(id))


def _total_price(prodid_list, u_id):
    totalPrice = 0
    for i in prodid_list:
        totalPrice += Product.objects.get(id=i).price * int(Cart.objects.get(user_id = u_id, product_id=i).quantity)
    totalPrice = round(totalPrice, 2)
    return totalPrice

@login_required()
def delete_from_cart(request, id):
    for x in Cart.objects.filter(user_id=request.user.id):
        if str(x) == str(id):
            product = get_object_or_404(Cart, pk=x.id)
            product.delete()

    return my_cart(request)

