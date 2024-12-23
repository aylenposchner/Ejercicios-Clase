from django.http import HttpResponse
from django.shortcuts import render

def saludar(request):
    return HttpResponse("Hola desde Django")

def index(request):
    return render(request, "core/index.html")

def tirar_dado(request):
    from datetime import datetime
    from random import randint

    tiro_de_dado = randint(1,6)

    if  tiro_de_dado == 6:
        mensaje = f"Has tirado el 🎲 y sacado un {tiro_de_dado}! ✨ Gananste ✨ "
    else:
        mensaje = f"Has tirado el 🎲 y sacado un {tiro_de_dado} Sigue intentando. Presiona F5"
    
    datos = {"title": "Tiro de datos", "mensaje": mensaje, "fecha": datetime.now}
    return render(request, "core/dados.html", context=datos)

def ejercicio1(request):
    nombre = "Aylen"
    apellido = "Poschner"
    datos1 = {
        "nombre":nombre,
        "apellido": apellido 
    }
    return render(request, "core/ejercicio1.html", context=datos1)

def ver_notas(request):
    lista_notas = [10,8,2,5,4]
    return render(request,"core/notas.html",{"notas":lista_notas})

def ejercicio2(request):
    usuarios = [{'nombre': 'juan', 'email': 'juan@django'},
        {'nombre': 'santi', 'email': 'santi@django'},
        {'nombre': 'agustín', 'email': 'agus@django'}]
    return render(request,"core/ejercicio2.html",{"usuarios":usuarios})
