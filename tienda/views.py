from django.shortcuts import render

# Create your views here.
def mangas(request):
    print("Hola estamos en la ventana mangas")
    context={}
    return render(request, 'tienda/mangas.html', context)

def index(request):
    print("Hola estamos en la ventana index")
    context={}
    return render(request, 'tienda/index.html', context)

def artbooks(request):
    print("Hola estamos en la ventana artbooks")
    context={}
    return render(request, 'tienda/artbooks.html', context)

def registrarse(request):
    print("Hola estamos en la ventana registrarse")
    context={}
    return render(request, 'tienda/registrarse.html', context)
def figuras(request):
    print("Hola estamos en la ventana figuras")
    context={}
    return render(request, 'tienda/figuras.html', context)
def contacto(request):
    print("Hola estamos en la ventana contacto")
    context={}
    return render(request, 'tienda/contacto.html', context)
