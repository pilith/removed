from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

# Models
from .models import component, fixed_board

# Forms
from .forms import componentForm, fixedForm

def index(request):
    return render(request, 'removed/index.html')

def removed(request):
    components = component.objects.all()
    return render(request, 'removed/removed.html', {'components':components})

def fixed(request):
    boards = fixed_board.objects.all()
    return render(request, 'removed/fixed.html', {'boards':boards})

def add_comp(request):
    if request.method != 'POST':
        form = componentForm()
    else:
        form = componentForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            import time
            year = time.strftime('%Y')[-2:]
            if not component.objects.all().count():
                new_entry.bag_id = year + '-' + str(1)
            else:
                last = component.objects.all().last()
                if  year == last.bag_id[:2]:
                    new_entry.bag_id = year + '-' + str(int(last.bag_id[3:]) + 1)
                else:
                    new_entry.bag_id = year + '-' + str(1)

            new_entry.save()
            messages.info(request, "Your bag id is: " + new_entry.bag_id)
            return HttpResponseRedirect(reverse('removed:removed'))

    return render(request, 'removed/add_comp.html', { 'form': form, })

def add_board(request):
    if request.method != 'POST':
        form = fixedForm()
    else:
        form = fixedForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('removed:fixed'))

    return render(request, 'removed/add_board.html', { 'form': form, })

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
