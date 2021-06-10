from django.urls import path
from . import views

urlpatterns = [
    path('cargaAcademica/', views.carga_academica, name="Carga Academica"),
    path('infoAlumno/', views.info_alumno, name="Info Alumno"),
    path('monitoreoGrupos/', views.monitoreo_grupos, name="Monitoreo Grupos"),
    path('inscripcion/', views.inscripcion, name="Inscripcion"),
    path('calificacionesAlumno/', views.calificaciones_alumno, name="Calificaciones Alumno"),
]