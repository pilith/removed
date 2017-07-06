from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import component
from .tables import ComponentTable

def index(request):
    return render(request, 'removed/index.html')

def removed(request):
    table = ComponentTable(component.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'removed/removed.html', {'table':table})

def fixed(request):
    return render(request, 'removed/fixed.html')

