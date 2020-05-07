from django.shortcuts import render, get_object_or_404, redirect
from game.models import Games, GameImage
from game.forms.game_form import GameCreateForm, GameUpdateForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        games = [ {
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.gameimage_set.first().image
        } for x in Games.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': games})
    context = {'games': Games.objects.all().order_by('name')}
    return render(request, 'game/index.html', context)

# /games/1
@login_required
def get_game_by_id(request, id):
    return render(request, 'game/game_details.html', {
        'game': get_object_or_404(Games, pk=id)
    })

@login_required
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

@login_required
def delete_game(request, id):
    game = get_object_or_404(Games, pk=id)
    game.delete()
    return redirect('game-index')

@login_required
def update_game(request, id):
    instance = get_object_or_404(Games, pk=id)
    if request.method == 'POST':
        form = GameUpdateForm(data=request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('game_details', id=id)
    else:
        form = GameUpdateForm(instance=instance)
    return render(request,'game/update_game.html',{
        'form': form,
        'id': id
    })