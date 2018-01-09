# base django imports
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

# app imports

from dnd.models import playerChar
from dnd.forms import charForm

# Create your views here.

def index(request):
    return render(request, 'dnd/index.html')


@login_required
def new_char(request):
    """ Making a new character"""
    if request.method == 'POST':
        form = charForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.user = request.user
            player.save()
        return HttpResponseRedirect(reverse('dnd:index'))

    else:
        form = charForm()

    return render(request, 'dnd/new_char.html', {'form': form})        
@login_required
def view_char(request, char_id):
    """ view an already created character"""
    character = playerChar.objects.get(pk=char_id)
    if request.user != character.user:
        raise PermissionDenied
    else:
        return render(request, 'dnd/view_char.html', {'character': character}) 

@login_required
def edit_char(request, char_id):
    """edit an already created character"""
    character = playerChar.objects.get(pk=char_id)
    if request.user != character.user:  # don't let other people edit someone elses characters
        raise PermissionDenied
    else:
        if request.method == 'POST':
            form = charForm(instance=character, data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('dnd:index'))
        else:
            form = charForm(instance=character)
    
        context = { 'character':character, 'form':form }
        return render(request, 'dnd/edit_char.html', context)
