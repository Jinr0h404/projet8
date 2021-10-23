from django.http import HttpResponse
from django.shortcuts import render, redirect
from User.forms import SignupForm, SigninForm
from django.contrib.auth import authenticate, login, logout

def index(request):
    #return HttpResponse("<h1>Du gras, oui, mais de qualité!</h1><h2>Site en construction, à très vite pour bien manger</h2>")
    return render(request, "User/index.html")

def signup(request):
    """on génère une instance de notre formulaire et on l'envoie formulaire via le context"""
    form = SignupForm()

    return render(request, "User/signup.html", context={'form': form})

def signin(request):
    form = SigninForm()
    message = ''
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username} !'
            else:
                message = 'Identifiants incorrects'
    return render(request, "User/signin.html", context={'form': form, 'message':message})

def logout_user(request):
    logout(request)
    return redirect("index")