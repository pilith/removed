from django.forms import ModelForm
from .models import boardgame

class gameForm(ModelForm):
    class Meta:
        model = boardgame
        exclude = ['owner']

