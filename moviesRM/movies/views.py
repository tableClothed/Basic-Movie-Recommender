from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Movie
import random

def home(response):
    # latest_movies = Movie.objects.order_by("popularity")[:9]
    # context = {"latest_movies":latest_movies}
    if response.user.is_authenticated:
        latest_movies = Movie.objects.filter(ratings__isnull=False).order_by('-ratings__average')[:9]
    else:
        movie_list = Movie.objects.all()
        latest_movies = random.sample(list(movie_list), 9)

    context = { "latest_movies": latest_movies }
    return render(response, "main/home.html", context)

def index(response, id):
    movie = Movie.objects.get(id=id)
    context = {"movie":movie}
    return render(response, "main/movie_detail.html", context)

def movie_list(response):
    pass

# def rate_list(request):
#     query = Rate.objects.filter(ratings__isnull=False).order_by('ratings__average')
#     context = { "movie_list": query }