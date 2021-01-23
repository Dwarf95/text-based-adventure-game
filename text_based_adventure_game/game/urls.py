from django.urls import path
from . import views

urlpatterns = {
    path('', views.index, name="index"),
    path('intro', views.intro, name="intro"),
    path('choose_path', views.choose_path, name="choose_path"),
    path('path_mountain', views.path_mountain, name="path_mountain"),
    path('path_mountain/<int:pk>', views.path_mountain_par, name="path_mountain_par"),
    path('path_slow_river', views.path_slow_river, name="path_slow_river"),
    path('path_slow_river/<int:pk>', views.path_slow_river_par, name="path_slow_river_par"),
}

