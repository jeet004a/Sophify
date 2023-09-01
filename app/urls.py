from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('home', views.index,name="home1"),
    path('login', views.login_page,name="login"),
    path('logout', views.logout_page,name="logout"),
    path('register', views.register,name="register"),
    path('profile/<str:id>/', views.profile,name="profile"),
    path('user/<str:id>',views.userform,name="user"),
    # path('details/<str:id>/',views.details,name="details"),
    
    # path('user/<str:id>/',views.usertest,name='user12')
]