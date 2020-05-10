from django.shortcuts import render

def my_cart(request):
    if request.method == 'GET':
        return render(request,'shopping_cart/my_cart.html')
