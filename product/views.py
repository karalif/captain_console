from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product, ProductImage, ReviewedItems
from product.forms.product_form import ProductCreateForm, ProductUpdateForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def get_product_by_id(request, id):
    id_list = []
    for x in ReviewedItems.objects.filter(user_id=request.user.id):
        id_list.append(x.id)
        if id == x.product_id:
            product = get_object_or_404(ReviewedItems, pk=x.id)
            product.delete()

    if len(ReviewedItems.objects.filter(user_id=request.user.id)) == 6:
        min_id = min(id_list)
        product = get_object_or_404(ReviewedItems, pk=min_id)
        product.delete()

    prod = []
    for x in ReviewedItems.objects.filter(user_id=request.user.id):
        prod.append(x)
    add_reviewed_item(request, id)
    context = {
        'product': get_object_or_404(Product, pk=id),
        'is_superuser': request.user.is_superuser,
        'reviewedItems': prod
    }
    return render(request, 'product/product_details.html', context)

@login_required
def add_reviewed_item(request,id):
    reviewed_item = ReviewedItems(user_id=request.user.id, product_id=id)
    reviewed_item.save()

@login_required
def create_product(request):
    if not request.user.is_superuser:
        # Gaetud sett 404 sidu her og alstadar i svona
        return redirect('/products')
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)
        if form.is_valid():
            product = form.save()
            product_image = ProductImage(image = request.POST['image'], product=product)
            product_image.save()
            return redirect('/products')
    else:
        form = ProductCreateForm(data=request.GET)
    return render(request, 'product/create_product.html', {
        'form': form
    })

@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if not request.user.is_superuser:
        return redirect('/products')
    product.delete()
    return redirect('/products')


@login_required
def update_product(request, id):
    instance = get_object_or_404(Product, pk=id)
    id_list=[]
    if not request.user.is_superuser:
        return redirect('/products')
    if request.method == 'POST':
        form = ProductUpdateForm(data=request.POST,instance=instance)
        if form.is_valid():
            product = form.save()
            product_image = ProductImage(image=request.POST['image'], product=product)
            print('image',type(product_image))
            if len(product_image.image)>0:
                product_image.save()
            for x in ProductImage.objects.filter(product_id=id):
                id_list.append(x.id)
            if len(id_list)==3:
                min_id=min(id_list)

                old_image=get_object_or_404(ProductImage, pk=min_id)
                old_image.delete()
            return redirect('product_details', id=id)
    else:
        form = ProductUpdateForm(instance=instance)
    return render(request,'product/update_product.html',{
        'form': form,
        'id': id
    })

#/products?type=
def home_index(request):
    new_prod_id = [1, 2, 5, 7, 8, 9, 10, 12]
    context = {'products': Product.objects.filter(id__in=new_prod_id)}
    return render(request, 'product/home_index.html', context)

def index(request):
    if "type_filter" in request.GET:

        type_filter = request.GET["type_filter"]
        if type_filter == 'price_high':
            context = {
                'products': Product.objects.all().order_by('price'),
                }
        elif type_filter == 'price_low':
            context = {
                'products': Product.objects.all().order_by('-price'),
                }
        elif type_filter=='name':
            context = {
                'products': Product.objects.all().order_by('name'),
                }
        else:
            context = {
                'products': Product.objects.filter(category_id=type_filter).order_by("name"),
                'category': True
            }
        return render(request, 'product/product_index.html', context)
    context={'products': Product.objects.all()}
    return render(request, 'product/index.html', context)


#/products/games?type=
def game_index(request):
    if "type_filter" in request.GET:
        type_filter = request.GET["type_filter"]
        if type_filter == 'price_high':
            context = {
                'products': Product.objects.filter(group_id=2).order_by('price')}
        elif type_filter == 'price_low':
            context = {
                'products': Product.objects.filter(group_id=2).order_by('-price')}
        elif type_filter=='name':
            context = {
                'products': Product.objects.filter(group_id=2).order_by('name')}
        else:
            context = {
                'products': Product.objects.filter(category_id=type_filter, group_id=2).order_by("name"),
                'title': 'Games',
                'category': True

            }
        return render(request, 'product/product_index.html', context)
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'age_limit': x.age_limit,
            'price': x.price,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search_filter,group_id=2)]
        return JsonResponse({'data': products})
    context = {'products': Product.objects.filter(group_id=2).order_by('name'), 'title': 'Games'}
    return render(request, 'product/product_index.html', context)


#/products/consoles?type=
def console_index(request):
    if "type_filter" in request.GET:
        type_filter=request.GET["type_filter"]
        print(type_filter)
        if type_filter=='price_low':
            context = {
                'products': Product.objects.filter(group_id=1).order_by('price')}
        elif type_filter == 'price_high':
            context = {
                'products': Product.objects.filter(group_id=1).order_by('-price')}
        elif type_filter=='name':
            context = {
                'products': Product.objects.filter(group_id=1).order_by('name')}
        else:
            context = {
                'products': Product.objects.filter(category_id=type_filter, group_id=1).order_by("name"),
                'title': 'Consoles',
                'category': True
            }
        return render(request, 'product/product_index.html', context)
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'price': x.price,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search_filter,group_id=1)]
        return JsonResponse({'data': products})
    context = {
        'products': Product.objects.filter(group_id=1).order_by('name'),
        'title': 'Consoles'
    }
    return render(request, 'product/product_index.html', context)