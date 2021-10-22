from django.http import HttpResponse
from django.shortcuts import render
from User.forms import SignupForm

def index(request):
    #return HttpResponse("<h1>Du gras, oui, mais de qualité!</h1><h2>Site en construction, à très vite pour bien manger</h2>")
    return render(request, "User/index.html")

def signup(request):
    """on génère une instance de notre formulaire et on l'envoie formulaire via le context"""
    form = SignupForm()

    return render(request, "User/signup.html", {'form': form})