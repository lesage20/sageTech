from django.urls import path
from .import views

urlpatterns = [
    path('single/<int:pk>', views.single, name="single"),
    path('tech/', views.tech, name="tech"),
    
]