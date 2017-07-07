from django.contrib import admin

# Register your models here.
from removed.models import component
from removed.models import fixed_board
admin.site.register(component)
admin.site.register(fixed_board)

