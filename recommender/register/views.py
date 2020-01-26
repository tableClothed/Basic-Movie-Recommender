from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForms

# Create your views here.
def register(response):

    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
        
        return redirect("/home")
    else:
        form = RegisterForms()

    return render(response, "register/register.html", {"form":form})