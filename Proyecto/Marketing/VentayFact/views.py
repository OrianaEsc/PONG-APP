from django.shortcuts import render

def Funcion(request):
    datos = {
        'nombre' : 'Estamos haciendo el proyecto'
    }

    return render (request, 'index.html', datos)

def contacto(request):
    datos = {}
    return render (request, 'contacto.html', datos)


def campanas(request):
    datos = {}
    return render (request, 'campanas.html', datos)

def nosotros(request):
    datos = {}
    return render (request, 'nosotros.html', datos)