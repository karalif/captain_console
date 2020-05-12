from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product, ProductImage
from product.forms.product_form import ProductCreateForm, ProductUpdateForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def home_index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [ {
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': products})
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'product/home_index.html', context)

def get_games(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [ {
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'age_limit': x.age_limit,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': products})
    context = {'products': Product.objects.filter(group_id=2).order_by('name')}
    return render(request, 'product/game_index.html', context)

def get_consoles(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [ {
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': products})
    context = {'products': Product.objects.filter(group_id=1).order_by('name')}
    return render(request, 'product/console_index.html', context)

# /games/1

def get_product_by_id(request, id):
    return render(request, 'product/product_details.html', {
        'product': get_object_or_404(Product, pk=id)
    })


@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            product = form.save()
            product_image = ProductImage(image = request.POST['image'], product=product)
            product_image.save()
            return redirect('product-index')
    else:
        form = ProductCreateForm()
    return render(request, '/create_product.html', {
        'form': form
    })

@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('product-index')

@login_required
def update_product(request, id):
    instance = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ProductUpdateForm(data=request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('product_details', id=id)
    else:
        form = ProductUpdateForm(instance=instance)
    return render(request,'product/update_product.html',{
        'form': form,
        'id': id
    })

def get_gameboy(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [ {
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'age_limit': x.age_limit,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': products})
    context = {'products': Product.objects.filter(category_id=1).order_by('name')}
    return render(request, 'product/gameboy_index.html', context)

def get_neo(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [ {
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'age_limit': x.age_limit,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': products})
    context = {'products': Product.objects.filter(category_id=2).order_by('name')}
    return render(request, 'product/neo_index.html', context)

def get_nes(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [ {
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'age_limit': x.age_limit,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': products})
    context = {'products': Product.objects.filter(category_id=3).order_by('name')}
    return render(request, 'product/nes_index.html', context)

def get_sega(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [ {
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'age_limit': x.age_limit,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': products})
    context = {'products': Product.objects.filter(category_id=4).order_by('name')}
    return render(request, 'product/sega_index.html', context)

def get_turbografix(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [ {
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'age_limit': x.age_limit,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': products})
    context = {'products': Product.objects.filter(category_id=5).order_by('name')}
    return render(request, 'product/turbografix_index.html', context)