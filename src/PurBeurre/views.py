from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("<h1>Du gras, oui, mais de qualité!</h1><h2>Site en construction, à très vite pour bien manger</h2>")
    return render(request, "PurBeurre/index.html")

def legal_notice(request):
    return render(request, "PurBeurre/legal_notice.html")