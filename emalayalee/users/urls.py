from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('userdash/',views.userdash, name='userdash'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
]