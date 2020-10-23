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