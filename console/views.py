from django.shortcuts import render
from console.models import Console

def index(request):
    context = {'consoles': Console.objects.all().order_by('name')}
    return render(request, 'console/index.html', context)
        #'consoles': Console.objects.all()

