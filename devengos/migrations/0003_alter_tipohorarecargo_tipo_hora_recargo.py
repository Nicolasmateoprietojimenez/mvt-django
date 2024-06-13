# Generated by Django 5.0.6 on 2024-06-12 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devengos', '0002_horaextra_nro_documento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipohorarecargo',
            name='tipo_hora_recargo',
            field=models.CharField(choices=[('extra_diurno', 'Hora extra diurno'), ('extra_nocturno', 'Hora extra nocturno'), ('extra_diurno_dominical_festivo', 'Hora extra diurno dominical y festivo'), ('extra_nocturno_dominical_festivo', 'Hora extra nocturno en domingos y festivos'), ('recargo_nocturno', 'recargo nocturno'), ('recargo_dominical_festivo', 'recargo dominical y festivo'), ('recargo_nocturno_dominical_festivo', 'recargo nocturno en dominical y festivo')], help_text='Tipo de hora con recargo', max_length=50),
        ),
    ]
