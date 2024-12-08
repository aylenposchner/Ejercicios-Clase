from django.shortcuts import render
from .models import Cliente

def ver_clientes(request):
    clientes = Cliente.objects.all()
    return render(request,"clientes/index.html",{"clientes":clientes})