from django.forms import ModelForm
from .models import playerChar

class charForm(ModelForm):
    class Meta:
        model = playerChar
        fields = '__all__' 

#['race', 'charclass', 'level', 'name', 
#                  'strength', 'dex', 'const', 'intel', 'wis', 
#                  'char', 'inspiration',
#                 ]

