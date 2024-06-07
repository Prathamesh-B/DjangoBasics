from django.urls import path
from base import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginPage, name='login'),
    path('register', views.registerPage, name='register'),
    path('form', views.formPage, name='form'),
    path('view', views.viewForms, name='view'),
    path('logout', views.logoutUser, name='logout'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('cam', views.cam, name='cam'),
    path('release_camera', views.release_camera, name='release_camera'),
]
