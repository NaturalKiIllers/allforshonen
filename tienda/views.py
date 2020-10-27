from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from .models import Figura
from .models import Manga
from .models import Artbook
from .models import Contacto
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

def agregar_figura(request):
    print("hola  estoy en agregar_figura...")
    if request.method == 'POST':
        var_codigo = request.POST['codigoF']
        var_nombre = request.POST['nombre']
        var_anime = request.POST['anime']
        var_descripcion = request.POST['descripcion']
        var_precio = request.POST['precio']
        var_altura = request.POST['altura']
        var_material = request.POST['material']
        var_tipo= request.POST['tipo']
        var_foto= request.FILES['foto']
        if var_codigo != "":
            try:
               figura = Figura()
               figura.codigof     = var_codigo
               figura.nombre     = var_nombre 
               figura.anime      = var_anime 
               figura.descripcion= var_descripcion
               figura.precio     = var_precio
               figura.altura     = var_altura 
               figura.material   = var_material
               figura.tipo       = var_tipo
               figura.foto       = var_foto
               figura.save()
               return render(request, 'personas/mensaje_datos_guardados.html',{})

            except figura.DoesNotExist:
               return render(request, 'personas/error/error_204.html', {})
        else:
           return render(request, 'personas/error/error_201.html', {})
    else:
        return render(request, 'personas/error/error_203.html', {})

def eliminar_figura(request):
    print("hola  estoy en eliminar_figura")
    if request.method == 'POST':
        var_codigo = request.POST['codigoF']
        if var_codigo != "":
           try:
               figura = Figura()
               figura= Figura.objects.get(codigof=var_codigo)
               if figura is not None:
                   print("figura=", figura)
                   figura.delete()
                   return render(request, 'personas/mensaje_alumno_eliminado.html', )
               else:
                   return render(request, 'personas/error/error_202.html',{})
           except figura.DoesNotExist:
               return render(request, 'personas/error/error_202.html', {})
        else:
           return render(request, 'personas/error/error_201.html', {})
    else:
        return render(request, 'personas/error/error_203.html', {})


def agregar_contacto(request):
    
    if request.method == 'POST':
        var_nombres = request.POST['nombres']
        var_correo  = request.POST['correo']
        var_asunto  = request.POST['asunto']
        var_mensaje = request.POST['mensaje']
        
        contacto = Contacto()
        contacto.nombres     = var_nombres
        contacto.correo      = var_correo 
        contacto.asunto      = var_asunto 
        contacto.mensaje     = var_mensaje
        contacto.save()
        return render(request,"tienda/index.html",{})
    else:
        return render(request, 'personas/error/error_203.html', {})

def administrador(request):
    print("Hola estamos en la ventana admin")
    context={}
    return render(request, 'tienda/administrador.html', context)

     
   
