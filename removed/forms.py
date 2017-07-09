from django import forms
from .models import component
from .models import fixed_board 

class componentForm(forms.ModelForm):
    class Meta:
        model = component
        fields = ['board', 'part_num', 'serial_num', 
                  'handling', 'notes']
        widgets = {'notes': forms.Textarea(attrs={'cols':80, 'rows':1})}


class fixedForm(forms.ModelForm):
    class Meta:
        model = fixed_board
        fields = ['board', 'serial_num', 'handling', 'notes']
        widgets = {'notes': forms.Textarea(attrs={'cols':40, 'rows':3})}

