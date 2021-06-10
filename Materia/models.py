from django.db import models
from Profesor.models import Profesor
from usuarios.models import Carrera
# Create your models here.

class Materia(models.Model):
    materia = models.CharField(max_length=50)
    hora_inicio = models.TimeField()
    hora_final = models.TimeField()
    aula = models.CharField(max_length=20)
    semestre = models.SmallIntegerField(default=1)

    class Meta:
        verbose_name = 'materia'
        verbose_name_plural = 'materias'
    def __str__(self):
        return self.materia

class Materias_carga_academica(models.Model):
    materia = models.ForeignKey(Materia,on_delete=True)
    profesor = models.ForeignKey(Profesor,on_delete=True)
    carrera = models.ForeignKey(Carrera,on_delete=True)
    class Meta:
        verbose_name = 'Materia carga academica'
        verbose_name_plural = 'Materias carga academica'
    def __str__(self):
        return self.materia.materia

class Unidad(models.Model):
    unidad = models.CharField(max_length=20)
    materia = models.ForeignKey(Materia,on_delete=True)
    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'
    def __str__(self):
        return self.materia.materia + ' -----> ' + self.unidad
