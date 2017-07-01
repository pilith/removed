from django.shortcuts import render

def removed(request):
    return render(request, 'removed/removed.html')
