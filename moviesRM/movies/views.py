from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Movie

def home(response):
    latest_movies = Movie.objects.order_by("popularity")[:9]
    context = {"latest_movies":latest_movies}
    return render(response, "main/home.html", context)