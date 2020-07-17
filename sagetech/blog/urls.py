from django.urls import path
from .import views



urlpatterns = [
    path('single/<int:pk>', views.single, name="single"),
    # path('like', views.like_view, name="like-article"),    
    path('', views.tech, name="tech"),
    
]