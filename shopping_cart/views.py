from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Cart

@login_required()
def my_cart(request):
    if request.method == 'GET':
        return render(request,'shopping_cart/my_cart.html')

@login_required()
def add_to_cart(request, id):
    cartitem = Cart(user_id=request.user.id, product_id=id)
    cartitem.save()
    return render(request, 'product/product_details.html', {
        'product': get_object_or_404(Product, pk=id)
    })

