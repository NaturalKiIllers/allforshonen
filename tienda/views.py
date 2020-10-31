from django.shortcuts import render , redirect
from django.contrib import admin
from django.urls import path, include
from .models import Figura
from .models import Manga
from .models import Artbook
from .models import Contacto
from . import views
from django.contrib.auth.decorators import login_required
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
    
def login(redirect):
    print("Hola estamos en la ventana de login")
    context={}
    return redirect(request, 'accounts/login.html', context)

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
               return render( request,'respuesta_crud/productos/agregado_corr.html',{})

            except figura.DoesNotExist:
               return render(request, 'respuesta_crud/productos/noexiste.html', {})
        else:
           return render(request, 'respuesta_crud/productos/Vacio.html', {})
    else:
        return render(request, 'respuesta_crud/productos/noexiste.html', {})

def eliminar_figura(request):
    print("hola  estoy en eliminar_figura")
    if request.method == 'POST':
        var_codigo = request.POST['codigof']
        if var_codigo != "":
           try:
               figura = Figura()
               figura= Figura.objects.get(codigof=var_codigo)
               if figura is not None:
                   print("figura=", figura)
                   figura.delete()
                   return render(request, 'respuesta_crud/productos/eliminar.html', )
               else:
                   return render(request, 'respuesta_crud/productos/noexiste.html',{})
           except figura.DoesNotExist:
               return render(request, 'respuesta_crud/productos/noexiste.html', {})
        else:
           return render(request, 'respuesta_crud/productos/Vacio.html', {})
    else:
        return render(request, 'respuesta_crud/productos/noexiste.html', {})


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
        return render(request,"tienda/adAgregar.html",{})
    else:
        return render(request, 'personas/error/error_203.html', {})

def administrador(request):
    print("Hola estamos en la ventana admin")
    figura= Figura.objects.all()
    context={ 'figuras':figura }
    return render(request, 'tienda/administrador.html', context)
   
def usuarios(request):
    print("Hola estamos en la ventana index")
    context={}
    return render(request, 'tienda/usuarios.html', context)

def MangaAg(request):
    print("Hola estamos en la ventana index")
    context={}
    return render(request, 'tienda/MangaAg.html', context)

def MangaEl(request):
    print("Hola estamos en la ventana index")
    context={}
    return render(request, 'tienda/MangaEl.html', context)

def MangaBu(request):
    
    print("Hola estamos en la ventana index")
    context={}
    return render(request, 'tienda/MangaBu.html', context)

   

def MangaL(request):
    print("Hola estamos en la ventana admin")
    manga= Manga.objects.all()
    context={ 'mangas':manga }
    return render(request, 'tienda/MangaL.html', context)  



def FiguraAg(request):
    print("Hola estamos en la ventana index")
    context={}
    return render(request, 'tienda/FiguraAg.html', context)

def FiguraEl(request):
    print("Hola estamos en la ventana index")
    context={}
    return render(request, 'tienda/FiguraEl.html', context)

def FiguraBu(request):
    print("Hola estamos en la ventana index")
    context={}
    return render(request, 'tienda/FiguraBu.html', context)

def FiguraL(request):
    print("Hola estamos en la ventana admin")
    figura= Figura.objects.all()
    context={ 'figuras':figura }
    return render(request, 'tienda/FiguraL.html', context)  



def ArtAg(request):
    print("Hola estamos en la ventana index")
    context={}
    return render(request, 'tienda/ArtAg.html', context)

def ArtEl(request):
    print("Hola estamos en la ventana index")
    context={}
    return render(request, 'tienda/ArtEl.html', context)

def ArtBu(request):
    print("Hola estamos en la ventana index")
    context={}
    return render(request, 'tienda/ArtBu.html', context)

def ArtL(request):
    print("Hola estamos en la ventana admin")
    artbook= Artbook.objects.all()
    context={ 'artbooks' : artbook}
    return render(request, 'tienda/ArtL.html', context)  



def FiguraEn(request):
   
    if request.method == 'POST':
        var_codigo = request.POST['codigof']
        if var_codigo != "":
           try:
                figura = Figura()
                figura= Figura.objects.get(codigof=var_codigo)
                if figura is not None:
                   context={'figura':figura}
                   return render(request, 'tienda/FiguraEn.html', context)
                else:
                   return render(request, 'respuesta_crud/productos/noexiste.html',{})
           except figura.DoesNotExist:
               return render(request, 'respuesta_crud/productos/noexiste.html', {})
        else:
           return render(request, 'respuesta_crud/productos/Vacio.html', {})
    else:
        return render(request, 'respuesta_crud/productos/Vacio.html', {})

def editar_figura(request):
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
               return render( request,'respuesta_crud/productos/modificar.html',{})

            except figura.DoesNotExist:
               return render(request, 'respuesta_crud/productos/noexiste.html', {})
        else:
           return render(request, 'respuesta_crud/productos/Vacio.html', {})
    else:
        return render(request, 'respuesta_crud/productos/Vacio.html', {})

def eliminar_manga(request):
    print("hola  estoy en eliminar_figura")
    if request.method == 'POST':
        var_codigo = request.POST['codigoM']
        if var_codigo != "":
           try:
               manga = Manga()
               manga= Manga.objects.get(codigoM=var_codigo)
               if manga is not None:
                   print("manga=", manga)
                   manga.delete()
                   return render(request, 'respuesta_crud/productos/eliminar.html', )
               else:
                   return render(request, 'respuesta_crud/productos/noexiste.html',{})
           except manga.DoesNotExist:
               return render(request, 'respuesta_crud/productos/noexiste.html', {})
        else:
           return render(request, 'respuesta_crud/productos/Vacio.html', {})
    else:
        return render(request, 'respuesta_crud/productos/Vacio.html', {})

def editar_manga(request):
    print("hola  estoy en agregar_figura...")
    if request.method == 'POST':
        var_id_manga = request.POST['id_manga']
        var_codigoM = request.POST['codigoM']
        var_nombre = request.POST['nombre']
        var_editorial = request.POST['editorial']
        var_tipo= request.POST['tipo']    
        var_precio = request.POST['precio']
        var_nombre_desc = request.POST['nombre_desc']
        var_descripcion = request.POST['descripcion']
        var_fotoManga= request.FILES['fotoM']
        if var_codigoM != "":
            try:
               manga = Manga()
               manga.id_manga         = var_id_manga
               manga.codigoM          = var_codigoM
               manga.nombre           = var_nombre 
               manga.editorial        = var_editorial
               manga.tipo             = var_tipo
               manga.precio           = var_precio
               manga.nombre_desc      = var_nombre_desc 
               manga.descripcion      = var_descripcion
               manga.fotoManga        = var_fotoManga
               manga.save()
               return render( request,'respuesta_crud/productos/modificar.html',{})

            except manga.DoesNotExist:
               return render(request, 'respuesta_crud/productos/noexiste.html', {})
        else:
           return render(request, 'respuesta_crud/productos/Vacio.html', {})
    else:
        return render(request, 'respuesta_crud/productos/Vacio.html', {})

def agregar_manga(request):
    print("hola  estoy en agregar_figura...")
    if request.method == 'POST':
        var_codigo = request.POST['codigoM']
        var_nombre = request.POST['nombre']
        var_editorial = request.POST['editorial']
        var_tipo= request.POST['tipo']    
        var_precio = request.POST['precio']
        var_nombre_desc = request.POST['nombre_desc']
        var_descripcion = request.POST['descripcion']
        var_fotoManga= request.FILES['fotoM']
        if var_codigo != "":
            try:
               manga = Manga()
               manga.codigoM          = var_codigo
               manga.nombre           = var_nombre 
               manga.editorial        = var_editorial
               manga.tipo             = var_tipo
               manga.precio           = var_precio
               manga.nombre_desc      = var_nombre_desc 
               manga.descripcion      = var_descripcion
               manga.fotoManga        = var_fotoManga
               manga.save()
               return render( request,'respuesta_crud/productos/agregado_corr.html',{})

            except manga.DoesNotExist:
               return render(request, 'respuesta_crud/productos/noexiste.html', {})
        else:
           return render(request, 'respuesta_crud/productos/Vacio.html', {})
    else:
        return render(request, 'respuesta_crud/productos/Vacio.html', {})

def MangaEn(request):
    if request.method == 'POST':
            var_codigo = request.POST['codigoM']
            if var_codigo != "":
                try:
                    manga = Manga()
                    manga= Manga.objects.get(codigoM=var_codigo)
                    if manga is not None:
                        context={'manga':manga}
                        return render(request, 'tienda/MangaEn.html', context)
                    else:
                        return render(request, '',{})
                except manga.DoesNotExist:
                    return render(request, 'respuesta_crud/productos/noexiste.html', {})
            else:
                return render(request, 'respuesta_crud/productos/Vacio.html', {})
    else:
        return render(request, 'respuesta_crud/productos/Vacio.html', {})


def agregar_art(request):
    print("hola  estoy en agregar_figura...")
    if request.method == 'POST':
        var_codigo = request.POST['codigoA']
        var_nombre = request.POST['nombre']
        var_precio = request.POST['precio']
        var_nombre_desc = request.POST['nombre_desc']
        var_descripcion = request.POST['descripcion']
        var_fotoArtbook     = request.FILES['fotoArtbook']
        if var_codigo != "":
            try:
               artbook = Artbook()
               artbook.codigoA         = var_codigo
               artbook.nombre           = var_nombre 
               artbook.precio           = var_precio
               artbook.nombre_desc      = var_nombre_desc 
               artbook.descripcion      = var_descripcion
               artbook.fotoArtbook      = var_fotoArtbook
               artbook.save()
               return render( request,'respuesta_crud/productos/agregado_corr.html',{})

            except artbook.DoesNotExist:
               return render(request, 'respuesta_crud/productos/noexiste.html', {})
        else:
           return render(request, 'respuesta_crud/productos/Vacio.html', {})
    else:
        return render(request, 'respuesta_crud/productos/Vacio.html', {})

def ArtEn(request):
    if request.method == 'POST':
            var_codigo = request.POST['codigoA']
            if var_codigo != "":
                try:
                    artbook = Artbook()
                    artbook= Artbook.objects.get(codigoA=var_codigo)
                    if artbook is not None:
                        context={'artbook':artbook}
                        return render(request, 'tienda/ArtEn.html', context)
                    else:
                        return render(request, 'personas/mensaje_alumno_elminado.html',{})
                except artbook.DoesNotExist:
                    return render(request, 'respuesta_crud/productos/noexiste.html', {})
            else:
                return render(request, 'respuesta_crud/productos/Vacio.html', {})
    else:
        return render(request, 'respuesta_crud/productos/Vacio.html', {})

def eliminar_art(request):
    if request.method == 'POST':
            var_codigo = request.POST['codigoA']
            if var_codigo != "":
                try:
                    artbook = Artbook()
                    artbook= Artbook.objects.get(codigoA=var_codigo)
                    if artbook is not None:
                        print("artbook =", artbook)
                        artbook.delete()
                        return render(request, 'respuesta_crud/productos/eliminar.html', {})
                    else:
                        return render(request, 'respuesta_crud/productos/noexiste.html',{})
                except artbook.DoesNotExist:
                    return render(request, 'respuesta_crud/productos/noexiste.html', {})
            else:
                return render(request, 'respuesta_crud/productos/noexiste.html', {})
    else:
        return render(request, 'respuesta_crud/productos/noexiste.html', {})

def editar_art(request):
    print("hola  estoy en modificar artbook...")
    if request.method == 'POST':
        var_id_artbook = request.POST['id_artbook']
        var_codigoA = request.POST['codigoA']
        var_nombre = request.POST['nombre']
        var_precio = request.POST['precio']
        var_nombre_desc = request.POST['nombre_desc']
        var_descripcion = request.POST['descripcion']
        var_fotoArtbook     = request.FILES['fotoArtbook']
        if var_codigoA != "":
            try:
               artbook = Artbook()
               artbook.id_artbook       = var_id_artbook
               artbook.codigoA         = var_codigoA
               artbook.nombre           = var_nombre 
               artbook.precio           = var_precio
               artbook.nombre_desc      = var_nombre_desc 
               artbook.descripcion      = var_descripcion
               artbook.fotoArtbook      = var_fotoArtbook
               artbook.save()
               return render( request,'respuesta_crud/productos/modificar.html',{})

            except artbook.DoesNotExist:
               return render(request, 'respuesta_crud/productos/noexiste.html', {})
        else:
           return render(request, 'respuesta_crud/productos/Vacio.html', {})
    else:
        return render(request, 'respuesta_crud/productos/Vacio.html', {})
