from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('movies/', views.movie_list, name="movies"),
    path('movies/<int:id>', views.index, name="index"),
]
