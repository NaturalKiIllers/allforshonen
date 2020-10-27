from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from .models import Figura
from .models import Manga
from .models import Artbook
from . import views

# Create your views here.
def mangas(request):
    print("Hola estamos en la ventana mangas")
    manga= Manga.objects.all()
    context={ 'mangas': manga}
    return render(request, 'tienda/mangas.html', context)

def index(request):
    print("Hola estamos en la ventana index")
    context={}
    return render(request, 'tienda/index.html', context)

def artbooks(request):
    print("Hola estamos en la ventana artbooks")
    artbook= Artbook.objects.all()
    context={ 'artbooks' : artbook}
    return render(request, 'tienda/artbooks.html', context)

def registrarse(request):
    print("Hola estamos en la ventana registrarse")
    context={}
    return render(request, 'tienda/registrarse.html', context)

def figuras(request):
    print("ok,estamos en la vista figura")
    figura= Figura.objects.all()
    context={ 'figuras':figura }
    return render(request, 'tienda/figuras.html', context)
    
def contacto(request):
    print("Hola estamos en la ventana contacto")
    context={}
    return render(request, 'tienda/contacto.html', context)

def admin(request):
    print("Hola estamos en la ventana del admin")
    context={}
    return render(request, 'tienda/admin.html', context)

def login(request):
    print("Hola estamos en la ventana de login")
    context={}
    return render(request, 'tienda/login.html', context)
