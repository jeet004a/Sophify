from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('login', views.login_page,name="login"),
    path('register', views.register,name="register"),
    path('user',views.user,name='user')
]