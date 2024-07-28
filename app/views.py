from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'app/index.html')

def curso(request):
    return render(request, 'app/curso.html')

def estudiantes(request):
    return render(request, 'app/estudiantes.html')

def profesores(request):
    return render(request, 'app/profesores.html')

def acerca(request):
    return render(request, 'app/acerca.html')

def formulario(request):
    return render(request, 'app/formulario.html')

