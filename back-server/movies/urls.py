from django.urls import path
from . import views


urlpatterns = [
    path('mainmovies/', views.main_movielist),
]