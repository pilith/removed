from django import forms
from .models import component

class componentForm(forms.ModelForm):
    class Meta:
        model = component
        fields = ['board', 'part_num', 'serial_num', 
                  'handling', 'notes']

