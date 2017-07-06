from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^removed_components$', views.removed, name='removed'),
    url(r'^fixed_list$', views.fixed, name='fixed'),
    url(r'^new_component$', views.add_comp, name='new_comp'),
]
