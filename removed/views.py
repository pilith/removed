from django.shortcuts import render
from django_tables2 import RequestConfig
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Models
from .models import component
from .models import fixed_board

# Tables
from .tables import ComponentTable
from .tables import boardTable

# Forms
from .forms import componentForm
from .forms import fixedForm

def index(request):
    return render(request, 'removed/index.html')

def removed(request):
    table = ComponentTable(component.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'removed/removed.html', {'table':table})

def fixed(request):
    table = boardTable(component.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'removed/fixed.html', {'table':table})

def add_comp(request):
    if request.method != 'POST':
        form = componentForm()
    else:
        form = componentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('removed:removed'))

    return render(request, 'removed/add_comp.html', {
        'form': form,
        })

def add_board(request):
    if request.method != 'POST':
        form = fixedForm()
    else:
        form = fixedForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('removed:fixed'))

    return render(request, 'removed/add_board.html', {
        'form': form,
        })
