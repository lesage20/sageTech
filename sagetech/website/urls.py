from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('', views.ArticleListView.as_view(), name='list'),
    path('contact/', views.contact, name="contact"),
    
    
    
]
