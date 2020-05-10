from django.shortcuts import render, get_object_or_404, redirect
from console.models import Console, ConsoleImage
from console.forms.console_form import ConsoleCreateForm, ConsoleUpdateForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        consoles = [ {
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.consoleimage_set.first().image
        } for x in Console.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': consoles})
    context = {'consoles': Console.objects.all().order_by('name')}
    return render(request, 'console/index.html', context)


# /console/1
@login_required
def get_console_by_id(request, id):
    return render(request, 'console/console_details.html', {
        'console': get_object_or_404(Console, pk=id)
    })


@login_required
def create_console(request):
    if request.method == 'POST':
        form = ConsoleCreateForm(data=request.POST)
        if form.is_valid():
            console = form.save()
            console_image = ConsoleImage(image = request.POST['image'], console=console)
            console_image.save()
            return redirect('console-index')
    else:
        form = ConsoleCreateForm()
    return render(request, 'console/create_console.html', {
        'form': form
    })


def delete_console(request, id):
    console = get_object_or_404(Console, pk=id)
    console.delete()
    return redirect('console-index')

def update_console(request, id):
    instance = get_object_or_404(Console, pk=id)
    if request.method == 'POST':
        form = ConsoleUpdateForm(data=request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('console_details', id=id)
    else:
        form = ConsoleUpdateForm(instance=instance)
    return render(request,'console/update_console.html',{
        'form': form,
        'id': id
    })