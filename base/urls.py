from django.urls import path
from base import views

urlpatterns = [
    path('', views.home ,name='home'),
    path('login', views.loginPage ,name='login'),
    path('register', views.registerPage ,name='register')
]