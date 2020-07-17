from django.urls import path 
from . import views


urlpatterns = [
    path('login', views.loginUser, name='login'),
    path('register', views.registerUser, name='register'),
    path('forgot-password', views.forgot, name='forgot-password'),
    path('logout', views.logoutUser, name='logout'),
    path('user-settings', views.Usettings, name='user-settings'),
    
    
]
