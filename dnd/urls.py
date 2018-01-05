# Views for dnd app. called from project 'settings.py'
from django.conf.urls import url
from . import views

app_name = 'dnd'
urlpatterns = [
    # home page
    url(r'^$', views.index, name='index'),
    url(r'^dnd/new$', views.new_char, name='new_char'),
    #url(r'^dnd/edit$', views.edit_char, name='edit_char'),
    
]

