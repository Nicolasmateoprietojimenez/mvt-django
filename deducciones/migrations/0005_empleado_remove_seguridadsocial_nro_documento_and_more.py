# Generated by Django 5.0.6 on 2024-06-16 23:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deducciones', '0004_alter_nivelriesgo_porcentaje_nivel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_documento', models.CharField(max_length=20, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('salario_basico', models.DecimalField(decimal_places=2, max_digits=10)),
                ('horas_extras', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='seguridadsocial',
            name='nro_documento',
        ),
        migrations.AlterField(
            model_name='nivelriesgo',
            name='porcentaje_nivel',
            field=models.CharField(choices=[('1', '0.348%'), ('2', '0.522%'), ('3', '1.044%'), ('4', '2.436%'), ('5', '6.960%')], help_text='Porcentaje del nivel de riesgo', max_length=100),
        ),
        migrations.AddField(
            model_name='seguridadsocial',
            name='empleado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='deducciones.empleado'),
        ),
    ]