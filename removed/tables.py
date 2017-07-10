import django_tables2 as tables

# Models
from .models import component
from .models import fixed_board

class ComponentTable(tables.Table):
    class Meta:
        model = component
        attrs = {'class': 'paleblue'}

class boardTable(tables.Table):
    class Meta:
        model = fixed_board
        attrs = {'class': 'paleblue'}


