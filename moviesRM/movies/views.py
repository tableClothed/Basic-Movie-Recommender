from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def home(response):
    return render(response, "main/home.html", {})