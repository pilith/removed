from django.shortcuts import render

def index(request):
    return render(request, 'removed/index.html')

def removed(request):
    return render(request, 'removed/removed.html')

def fixed(request):
    return render(request, 'removed/fixed.html')
