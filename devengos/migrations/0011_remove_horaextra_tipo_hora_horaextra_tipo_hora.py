# Generated by Django 5.0.6 on 2024-06-12 23:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devengos', '0010_remove_horaextra_tipo_hora_horaextra_tipo_hora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horaextra',
            name='tipo_Hora',
        ),
        migrations.AddField(
            model_name='horaextra',
            name='tipo_Hora',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='devengos.tipohorarecargo'),
        ),
    ]
