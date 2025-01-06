from django.urls import path
from .views import RegisterView, LoginView
from . import views

urlpatterns = [

    path('', views.blog_list, name='blog_list'),
    path('<int:id>/', views.blog_detail, name='blog_detail'),
    path('create_post/', views.create_post, name='create_post'),  # Create post page URL
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home')
]
