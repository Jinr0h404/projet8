from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Du gras, oui, mais de qualité!</h1><h2>Site en construction, à très vite pour bien manger</h2>")