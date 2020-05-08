from django.shortcuts import render, get_object_or_404, redirect
from console.models import Console
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        consoles = [ {
            'id': x.id,
            'name': x.name,
            'description': x.description,
        } for x in Console.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': games})
    context = {'consoles': Console.objects.all().order_by('name')}
    return render(request, 'console/index.html', context)

# /games/1
@login_required
def get_console_by_id(request, id):
    return render(request, 'console/console_details.html', {
        'console': get_object_or_404(Console, pk=id)
    })