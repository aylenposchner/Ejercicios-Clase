from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def saludar(request):
    return HttpResponse("Hola desde Django")

def index(request):
    return render(request, "core/index.html")