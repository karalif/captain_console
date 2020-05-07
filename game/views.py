from django.shortcuts import render, get_object_or_404
from game.models import Games

def index(request):
    context = {'games': Games.objects.all().order_by('name')}
    return render(request, 'game/index.html', context)

# /games/1
def get_game_by_id(request, id):
    return render(request, 'game/game_details.html', {
        'game': get_object_or_404(Games, pk=id)
    })


