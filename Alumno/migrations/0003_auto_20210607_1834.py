# Generated by Django 2.1.15 on 2021-06-07 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumno', '0002_auto_20210607_1214'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carga_academica_alumno',
            options={'verbose_name': 'Carga academica alumno', 'verbose_name_plural': 'Carga academica alumnos'},
        ),
        migrations.AlterModelOptions(
            name='detalle_carga_alumno',
            options={'verbose_name': 'Detalle carga academica alumno', 'verbose_name_plural': 'Detalle carga academica alumnos'},
        ),
        migrations.AlterField(
            model_name='detalle_carga_alumno',
            name='materia_ca',
            field=models.ForeignKey(on_delete=True, to='Materia.Materias_carga_academica'),
        ),
    ]
