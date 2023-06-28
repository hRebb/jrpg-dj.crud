from django.shortcuts import render, redirect
from models import Game

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
        return redirect('jrpg/game_list.html')
    return render(
        request,
        'jrpg/add_game.html'
    )