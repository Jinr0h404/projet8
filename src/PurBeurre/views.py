from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "PurBeurre/index.html")

def legal_notice(request):
    return render(request, "PurBeurre/legal_notice.html")