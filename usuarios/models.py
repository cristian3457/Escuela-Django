from django.db import models
from django.contrib.auth.models import AbstractUser

tipo_usuario = (
    ('ADMINISTRADOR', 'ADMINISTRADOR'),
    ('ALUMNO', 'ALUMNO'),
    ('DOCENTE', 'DOCENTE'),
    ('COORDINADOR', 'COORDINADOR'),
)
class Usuario(AbstractUser):
    tipo = models.CharField(max_length=20, choices=tipo_usuario)

class Carrera(models.Model):
    carrera = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'carrera'
        verbose_name_plural = 'carreras'
    def __str__ (self):
        return self.carrera

class Coordinador(models.Model):
    nombre =  models.CharField(max_length=50)
    apellidos =  models.CharField(max_length=50)
    carrera =  models.ForeignKey(Carrera, on_delete=True)
    usuario =  models.ForeignKey(Usuario, on_delete=True)
        
    class Meta:
        verbose_name = 'coordinador'
        verbose_name_plural = 'coordinadores'
    def __str__(self):
        return self.nombre + ' ' + self.apellidos


    
