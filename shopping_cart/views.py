from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product, ProductImage
from product.forms.product_form import ProductCreateForm, ProductUpdateForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required()
def my_cart(request):
    if request.method == 'GET':
        return render(request,'shopping_cart/my_cart.html')

@login_required()
def add_to_cart(request,id):
    print(id)
    print(request.user.username)
    return render(request, 'product/product_details.html', {
        'product': get_object_or_404(Product, pk=id)
    })
