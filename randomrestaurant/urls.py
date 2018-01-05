from django.urls import path, include
from django.contrib import admin
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('removed/',include('removed.urls', namespace='removed')),
    path('random/', include('restaurants.urls', namespace='restaurants')),
    path('dnd/', include('dnd.urls', namespace='dnd')),

    # account paths for login, logout, password management
    path('signup/', accounts.views.signup),
    path('accounts/', include('django.contrib.auth.urls')),
]

