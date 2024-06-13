# Generated by Django 5.0.6 on 2024-06-12 22:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deducciones', '0002_seguridadsocial_nro_documento_and_more'),
        ('gestion_empleados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='nivel_riesgo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='deducciones.nivelriesgo'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='salario_base',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
