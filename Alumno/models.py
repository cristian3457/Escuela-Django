from django.db import models
from usuarios.models import Carrera, Usuario
from Materia.models import Materias_carga_academica, Unidad
# Create your models here.

class Alumno(models.Model):
    nombre =  models.CharField(max_length=50)
    apellidos =  models.CharField(max_length=50)
    carrera =  models.ForeignKey(Carrera, on_delete=True)
    fecha_inscripcion = models.DateField()
    semestre = models.IntegerField( default=1)
    usuario =  models.ForeignKey(Usuario, on_delete=True)

    class Meta:
        verbose_name = 'alumno'
        verbose_name_plural = 'alumnos'
    def __str__(self):
        return self.nombre + ' ' + self.apellidos

class Carga_academica_alumno(models.Model):
    alumno = models.ForeignKey(Alumno,on_delete=True)
    
    class Meta:
        verbose_name = 'Carga academica alumno'
        verbose_name_plural = 'Carga academica alumnos'
    def __str__(self):
        return self.alumno.nombre + ' ' + self.alumno.apellidos + '  ------>  ' + self.alumno.usuario.username + '  ------>  Semestre: ' + str(self.alumno.semestre)

class Detalle_carga_alumno(models.Model):
    materia_ca = models.ForeignKey(Materias_carga_academica,on_delete=True)
    carga_academica_alumno = models.ForeignKey(Carga_academica_alumno,on_delete=True)

    class Meta:
        verbose_name = 'Detalle carga academica alumno'
        verbose_name_plural = 'Detalle carga academica alumnos'
    def __str__(self):
        return self.carga_academica_alumno.alumno.nombre + ' ' + self.carga_academica_alumno.alumno.apellidos + ' ------> ' + self.materia_ca.materia.materia


class Calificacion(models.Model):
    unidad = models.ForeignKey(Unidad,on_delete=True)
    alumno = models.ForeignKey(Alumno,on_delete=True)
    calificacion = models.SmallIntegerField(default=0)
    class Meta:
        verbose_name = 'Calificacion'
        verbose_name_plural = 'Calificaciones'
    def __str__(self):
        return self.alumno.nombre + ' ' + self.alumno.apellidos + ' -----> ' + self.unidad.unidad + ' -----> ' + str(self.calificacion)