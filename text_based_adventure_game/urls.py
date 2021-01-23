from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('text_based_adventure_game.game.urls')),
    path('admin/', admin.site.urls),
]
