# Generated by Django 2.1.15 on 2021-06-07 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profesor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=50)),
                ('hora_inicio', models.DateTimeField(auto_now_add=True)),
                ('hora_final', models.DateTimeField(auto_now_add=True)),
                ('aula', models.CharField(max_length=20)),
                ('semestre', models.SmallIntegerField(default=1)),
            ],
            options={
                'verbose_name': 'materia',
                'verbose_name_plural': 'materias',
            },
        ),
        migrations.CreateModel(
            name='Materias_carga_academica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.ForeignKey(on_delete=True, to='Materia.Materia')),
                ('profesor', models.ForeignKey(on_delete=True, to='Profesor.Profesor')),
            ],
            options={
                'verbose_name': 'materia_carga_academica',
                'verbose_name_plural': 'materias_carga_academica',
            },
        ),
    ]