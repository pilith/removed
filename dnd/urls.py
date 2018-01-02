# Views for dnd app. called from project 'settings.py'
from django.conf.urls import url
from . import views
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

app_name = 'dnd'
urlpatterns = [
    # home page
    url(r'^$', views.index, name='index'),
    url(r'^register/$', CreateView.as_view(
        template_name='register.html',
        form_class = UserCreationForm,
        success_url='/'),
        name='register'),
    url(r'^dnd/new$', views.new_char, name='new_char'),
    #url(r'^dnd/edit$', views.edit_char, name='edit_char'),
    
]

