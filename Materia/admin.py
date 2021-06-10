from Alumno.models import Calificacion
from django.contrib import admin
from django.contrib.admin.sites import site
from .models import Materia, Materias_carga_academica, Unidad
# Register your models here.

class Admin_materia(admin.ModelAdmin):
    list_display = ('materia','hora_inicio','hora_final', 'aula','semestre')

class Admin_materias_carga_academica(admin.ModelAdmin):
    list_display = ('materia','profesor')

admin.site.register(Materia,Admin_materia)
admin.site.register(Materias_carga_academica, Admin_materias_carga_academica)

admin.site.register(Unidad)
admin.site.register(Calificacion)