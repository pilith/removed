from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # tables
    url(r'^removed_components$', views.removed, name='removed'),
    url(r'^fixed_list$', views.fixed, name='fixed'),

    # new entries
    url(r'^removed_components/new$', views.add_comp, name='add_comp'),
    url(r'^fixed_list/new$', views.add_board, name='add_board'),
]
