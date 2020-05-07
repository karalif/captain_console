from django.shortcuts import render, get_object_or_404, redirect
from game.models import Games, GameImage
from game.forms.game_form import GameCreateForm

def index(request):
    context = {'games': Games.objects.all().order_by('name')}
    return render(request, 'game/index.html', context)

# /games/1
def get_game_by_id(request, id):
    return render(request, 'game/game_details.html', {
        'game': get_object_or_404(Games, pk=id)
    })

def create_game(request):
    if request.method == 'POST':
        form = GameCreateForm(data=request.POST)
        if form.is_valid():
            game = form.save()
            game_image = GameImage(image = request.POST['image'], game=game)
            game_image.save()
            return redirect('game-index')
    else:
        form = GameCreateForm()
    return render(request, 'game/create_game.html', {
        'form': form
    })

def delete_game(request, id):
    game = get_object_or_404(Games, pk=id)
    game.delete()
    return redirect('game-index')