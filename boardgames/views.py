# base django imports
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

# app imports

from boardgames.models import boardgame
from boardgames.forms import gameForm

# Create your views here.

def index(request):
    return render(request, 'boardgames/index.html')


@login_required
def new_game(request):
    """ Add a new boardgame to your backpack"""
    if request.method == 'POST':
        form = gameForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.owner = request.user
            player.save()
        return HttpResponseRedirect(reverse('boardgames:index'))

    else:
        form = gameForm()

    return render(request, 'boardgames/new_game.html', {'form': form})        

@login_required
def edit_game(request, game_id):
    """edit an already created character"""
    boardg = boardgame.objects.get(pk=game_id)
    if request.user != game.owner:  # don't let other people edit someone elses characters
        raise PermissionDenied
    else:
        if request.method == 'POST':
            form = gameForm(instance=game, data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('boardgames:index'))
        else:
            form = gameForm(instance=game)
    
        context = { 'game': game, 'form':form }
        return render(request, 'boardgames/edit_game.html', context)
