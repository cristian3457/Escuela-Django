# Generated by Django 2.1.15 on 2021-06-09 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Materia', '0004_materias_carga_academica_carrera'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad', models.CharField(max_length=20)),
                ('materia', models.ForeignKey(on_delete=True, to='Materia.Materia')),
            ],
            options={
                'verbose_name': 'Unidad',
                'verbose_name_plural': 'Unidades',
            },
        ),
    ]