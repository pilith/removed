from django.shortcuts import render
from django_tables2 import RequestConfig
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Models
from .models import component, fixed_board

# Tables
from .tables import ComponentTable, boardTable

# Forms
from .forms import componentForm, fixedForm

def index(request):
    return render(request, 'removed/index.html')

def removed(request):
    table = ComponentTable(component.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'removed/removed.html', {'table':table})

def fixed(request):
    table = boardTable(fixed_board.objects.all())
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

def edit_comp(request, comp_id):
    entry = component.objects.get(id=comp_id)

    if request.method != 'POST':
        form = componentForm(instance=entry)
    else:
        form = componentForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('removed:removed'))

    context = { 'entry':entry, 'form':form }
    return render(request, 'removed/edit_comp.html', context)
