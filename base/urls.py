from django.urls import path
from base import views

urlpatterns = [
    path('', views.home ,name='home'),
    path('login', views.login ,name='login'),
    path('register', views.register ,name='register')
]