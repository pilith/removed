# base django imports
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# app imports

from dnd.models import playerChar
from dnd.forms import charForm

# Create your views here.

def index(request):
    return render(request, 'dnd/index.html')


@login_required
def new_char(request):
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

#def edit_char(request):
