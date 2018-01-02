# Views for restaurants app. called from project 'settings.py'

from django.conf.urls import url
from . import views

app_name = 'restaurants'
urlpatterns = [
    # home page
    url(r'^$', views.index, name='index'),
    # other random food pages
    url(r'^dinner/$', views.dinner, name='dinner'),
    url(r'^breakfast/$', views.breakfast, name='breakfast'),
    url(r'^credits/$', views.credits, name='credits'),
]

