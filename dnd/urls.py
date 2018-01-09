# Views for dnd app. called from project 'settings.py'
from django.urls import path, re_path
from . import views

app_name = 'dnd'
urlpatterns = [

    path('', views.index, name='index'),
    path('dnd/new', views.new_char, name='new_char'),
    re_path('dnd/edit/(?P<char_id>\d+)$', views.edit_char, name='edit_char'),
    re_path('dnd/view/ (?P<char_id>\d+)$', views.view_char, name='view_char'), 
]

