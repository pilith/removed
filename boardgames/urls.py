# Views for boardgames app. called from project 'settings.py'
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'boardgames'
urlpatterns = [

    path('', views.index, name='index'),
    path('boardgames/new', views.new_game, name='new_game'),
    re_path('boardgames/edit/(?P<char_id>\d+)$', views.edit_game, name='edit_game'),
]
