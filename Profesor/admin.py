from django.contrib import admin
from .models import Profesor
# Register your models here.

class Admin_profesor(admin.ModelAdmin):
    list_display = ('nombre','apellidos','carrera')

admin.site.register(Profesor, Admin_profesor)