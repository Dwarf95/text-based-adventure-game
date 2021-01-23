from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('intro', views.intro, name="intro"),
    path('choose_path', views.choose_path, name="choose_path"),
    path('path_mountain', views.path_mountain, name="path_mountain"),
    path('path_mountain/path_mountain_first_choice', views.path_mountain_first_choice, name="path_mountain_first_choice"),
    path('path_slow_river', views.path_mountain, name="path_slow_river"),
]
