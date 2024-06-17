# Generated by Django 5.0.6 on 2024-06-16 23:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deducciones', '0005_empleado_remove_seguridadsocial_nro_documento_and_more'),
        ('gestion_empleados', '0008_delete_tokenaccess'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seguridadsocial',
            name='empleado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seguridad_social', to='gestion_empleados.empleado'),
        ),
        migrations.DeleteModel(
            name='Empleado',
        ),
    ]