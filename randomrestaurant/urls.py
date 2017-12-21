from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^removed/', include('removed.urls', namespace='removed')),
    url(r'^random/', include('restaurants.urls', namespace='restaurants')),
    url(r'^dnd/', include('dnd.urls', namespace='dnd')),

    # account URLs for login, logout, password management
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

