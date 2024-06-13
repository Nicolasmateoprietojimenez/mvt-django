# Generated by Django 5.0.6 on 2024-06-12 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deducciones', '0002_seguridadsocial_nro_documento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nivelriesgo',
            name='porcentaje_nivel',
            field=models.DecimalField(choices=[('1', '0,348%'), ('2', '0,522%'), ('3', '1,044%'), ('4', '2,436%'), ('5', '6,960%')], decimal_places=2, help_text='Porcentaje del nivel de riesgo', max_digits=5),
        ),
    ]
