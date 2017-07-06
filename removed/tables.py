import django_tables2 as tables
from .models import component

class ComponentTable(tables.Table):
    class Meta:
        model = component
        attrs = {'class': 'paleblue'}
