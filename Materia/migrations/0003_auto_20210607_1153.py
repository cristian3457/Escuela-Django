# Generated by Django 2.1.15 on 2021-06-07 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Materia', '0002_auto_20210607_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='hora_final',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='materia',
            name='hora_inicio',
            field=models.TimeField(),
        ),
    ]