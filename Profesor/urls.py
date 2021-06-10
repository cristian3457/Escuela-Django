from django.urls import path
from . import views

urlpatterns = [
    path('profesor/', views.profesor, name="Profesor"),
    path('cargaProfesor/', views.carga_profesor, name="Carga Profesor"),
    path('infoProfesor/', views.info_docente, name="Info Profesor"),
    path('alumnosMateria/', views.alumnos_materia, name="Alumnos Materia"),
    path('alumnosMateria/<int:id_materia>/', views.alumnos_materia_id, name="Alumnos Materia ID"),
    path('subirCalificaciones/', views.subir_calificaciones, name="Subir Calificaciones"),
    path('subirCalificaciones/<int:id_materia>/', views.subir_calificaciones_id, name="Subir Calificaciones ID"),
    path('subir/<int:id_materia>/', views.subir, name="Subir"),
]