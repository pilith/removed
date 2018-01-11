from django.urls import path, include, re_path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('removed/',include('removed.urls', namespace='removed')),
    path('random/', include('restaurants.urls', namespace='restaurants')),
    path('dnd/', include('dnd.urls', namespace='dnd')),
    path('boardgames', include('boardgames.urls', namespace='boardgames')),    

    # account paths for login, logout, password management
    path('signup/', accounts.views.signup),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # for development - remove for production

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,}),
    ] # for serving media during dev - not hardened for production
