from django.shortcuts import render, redirect, get_object_or_404
from .models import Game

# Create your views here.


def game_list(request):
    games = Game.objects.all()
    return render(
        request,
        'jrpg/game_list.html',
        {
            'games': games
        }
    )


def add_game(request):
    if request.method == 'POST':
        name = request.POST['name']
        publisher = request.POST['publisher']
        console = request.POST['console']
        adaptation = request.POST['adaptation']
        game = Game(
            name=name,
            publisher=publisher,
            console=console,
            adaptation=adaptation
        )
        game.save()
        return redirect('game_list')
    return render(
        request,
        'jrpg/add_game.html'
    )


def edit_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)

    if request.method == 'POST':
        game.name = request.POST['name']
        game.publisher = request.POST['publisher']
        game.console = request.POST['console']
        game.adaptation = request.POST['adaptation']
        game.save()
        return redirect('game_list')

    return render(
        request,
        'jrpg/edit_game.html',
        {
            'game': game
        }
    )

def delete_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)

    if request.method == 'POST':
        game.delete()
        return redirect('game_list')

    return render(
        request,
        'jrpg/delete_game.html',
        {
            'game': game
        }
    )