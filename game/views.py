from django.shortcuts import render

from game.models import Games

def index(request):
    context = {'games': Games.objects.all().order_by('name')}
    return render(request, 'game/index.html', context)



