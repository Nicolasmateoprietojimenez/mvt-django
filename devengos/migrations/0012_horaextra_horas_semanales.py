# Generated by Django 5.0.6 on 2024-06-12 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devengos', '0011_remove_horaextra_tipo_hora_horaextra_tipo_hora'),
    ]

    operations = [
        migrations.AddField(
            model_name='horaextra',
            name='horas_Semanales',
            field=models.CharField(blank=True, choices=[('42', '42 Horas'), ('43', '43 Horas'), ('44', '44 Horas'), ('45', '45 Horas'), ('46', '46 Horas'), ('47', '47 Horas')], help_text='Horas semanales Trbajadas', max_length=3, null=True),
        ),
    ]
