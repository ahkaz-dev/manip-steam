from django.contrib import admin
from django.urls import path, include
from manipsteam import views


urlpatterns = [
    path('', views.home, name='home'),
    path('game/<int:game_appid>/', views.game_info, name='game_info'),
]
