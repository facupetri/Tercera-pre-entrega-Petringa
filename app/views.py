from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Curso, Estudiante, Profesor


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

def formulario_cursos(request):
    if request.method == 'POST':
        curso_nombre = request.POST.get('nombre')
        comision_str = request.POST.get('comision')
        
        
        if curso_nombre and comision_str.isdigit():
            comision_int = int(comision_str)  
            nuevo_curso = Curso(nombre = curso_nombre, comision = comision_int)
            nuevo_curso.save()
            return render(request, 'app/curso.html')
        
        else:
            mensaje = 'Algo hiciste mal'
            return render(request, 'app/curso.html', {'error_message': mensaje})
        
    return render(request, 'app/curso.html')

def formulario_profesores(request):
    if request.method == 'POST':
        profesor_nombre = request.POST.get('nombre')
        apellido_str = request.POST.get('apellido')
        materia_str = request.POST.get('materia')

        nuevo_profesor = Profesor(nombre=profesor_nombre, apellido=apellido_str, materia=materia_str)
        nuevo_profesor.save()
        return render(request, 'app/profesores.html')
    
    return render(request, 'app/profesores.html')

def formulario_estudiantes(request):
    if request.method == 'POST':
        estudiante_nombre = request.POST.get('nombre')
        apellido_st = request.POST.get('apellido')
        email_str = request.POST.get('email')
        
        nuevo_estudiante = Estudiante(nombre=estudiante_nombre, apellido=apellido_st, email=email_str)
        nuevo_estudiante.save()
        return render(request, 'app/estudiantes.html')
    
    return render(request, 'app/estudiantes.html')

def buscar_curso(request):
    if 'curso' in request.GET and request.GET['curso']:
        comision = request.GET.get('comision', '') 
        curso = request.GET['curso']
        cursos = Curso.objects.filter(nombre__icontains=curso)

        return render(request, 'app/resultados_curso.html', {'query': cursos, 'comision': comision})
    else:
        respuesta = 'No existen datos'
        return HttpResponse(respuesta)

def buscar_profesor(request):
    if request.GET['nombre']:
        profesor = request.GET['nombre']
        profesores = Profesor.objects.filter(nombre__icontains=profesor)

        return render(request, "app/resultados_profesor.html",{'profesores':profesores, 'query':profesor })
    else:
        respuesta2 = 'no has introducido nada'
    return HttpResponse(respuesta2)
    
def buscar_estudiante(request):
    if request.GET['nombre']:
        estudiante = request.GET['nombre']
        estudiantes = Estudiante.objects.filter(nombre__icontains=estudiante)

        return render(request, "app/resultados_estudiante.html",{'estudiantes':estudiantes, 'query':estudiante })
    else:
        respuesta3 = 'no has introducido nada'
    return HttpResponse(respuesta3)