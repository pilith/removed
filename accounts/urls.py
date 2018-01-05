from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    # home page
    # path('', views.index, name='index'),
    path('signup/', views.signup),    
]

