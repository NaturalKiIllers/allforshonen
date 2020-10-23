from django.shortcuts import render

# Create your views here.
def prueba(request):
    print("Hola estamos en una prueba")
    context={}
    return render(request, 'tienda/prueba.html', context)