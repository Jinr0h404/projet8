from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Du gras, oui, mais de qualité!</h1><h2>Ici vous trouverez vos favoris</h2>")