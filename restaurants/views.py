from django.shortcuts import render
from cowpy import cow
import random

# Create your views here.

def index(request):
    """The home and lunch page for random restaurants"""
    lunches = [ "ginos", "five guys", "culvers", 
            "noodles inc", "which wich", "milios",
            "freska", "dickies", 
            "jimmy johns", "jersey mikes" ]
    lunch_cow = cow.www(thoughts=True)
    destination = lunch_cow.milk(random.choice(lunches))
    context = {'destination':destination}
    return render(request, 'restaurants/index.html', context)

def dinner(request):
    return render(request, 'restaurants/dinner.html')

def breakfast(request):
    return render(request, 'restaurants/breakfast.html')

def credits(request):
    return render(request, 'restaurants/credits.html')

