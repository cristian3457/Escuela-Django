from django.db import models
from usuarios.models import Carrera, Usuario
# Create your models here.

class Profesor(models.Model):
    nombre =  models.CharField(max_length=50)
    apellidos =  models.CharField(max_length=50)
    carrera =  models.ForeignKey(Carrera, on_delete=True)
    usuario =  models.ForeignKey(Usuario, on_delete=True)

    class Meta:
        verbose_name = 'profesor'
        verbose_name_plural = 'profesores'
    def __str__(self):
        return self.nombre + ' ' + self.apellidos

