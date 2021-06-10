from Alumno.models import Alumno, Carga_academica_alumno, Detalle_carga_alumno
from django.contrib import admin

# Register your models here.

class Admin_alumno(admin.ModelAdmin):
    list_display = ('nombre','apellidos','carrera','semestre','fecha_inscripcion')


admin.site.register(Alumno, Admin_alumno)
admin.site.register(Carga_academica_alumno)
admin.site.register(Detalle_carga_alumno)