from django.urls import path

from .views import inicio, curso, estudiantes, profesores, acerca, formulario_cursos, formulario_profesores, formulario_estudiantes, buscar_curso, buscar_estudiante, buscar_profesor

urlpatterns = [
    path('', inicio, name='inicio'),
    path('curso', curso, name='curso'),
    path('profesores', profesores, name='profesores'),
    path('estudiantes', estudiantes, name='estudiantes'),
    path('acerca', acerca, name='acerca'),
    path('formulario_cursos', formulario_cursos, name='formulario_cursos'),
    path('formulario_profesores', formulario_profesores, name='formulario_profesores'),
    path('formulario_estudiantes', formulario_estudiantes, name='formulario_estudiantes'),
    path('buscar_curso', buscar_curso),
    path('buscar_estudiante', buscar_estudiante),
    path('buscar_profesor', buscar_profesor),

]