from django.db import models

# Create your models here.


class TipoHoraRecargo(models.Model):
    
    TIPOS_HORA_RECARGO = [
        ('extra_diurno', 'Hora extra diurno'),
        ('extra_nocturno', 'Hora extra nocturno'),
        ('extra_diurno_dominical_festivo', 'Hora extra diurno dominical y festivo'),
        ('extra_nocturno_dominical_festivo', 'Hora extra nocturno en domingos y festivos'),
        ('recargo_nocturno', 'recargo nocturno'),
        ('recargo_dominical_festivo', 'recargo dominical y festivo'),
        ('recargo_nocturno_dominical_festivo', 'recargo nocturno en dominical y festivo'),
    ]

    tipo_hora_recargo = models.CharField(max_length=50, choices=TIPOS_HORA_RECARGO, help_text="Tipo de hora con recargo")
    porc_hora_recargo = models.DecimalField(max_digits=5, decimal_places=2, help_text="Porcentaje del recargo de la hora")

    def __str__(self):
        return f"{self.get_tipo_hora_recargo_display()} - {self.porc_hora_recargo}%"

class HoraExtra(models.Model):

    nro_documento = models.ForeignKey('gestion_empleados.Empleado', on_delete=models.CASCADE, null=True)

    fecha_hora = models.DateTimeField(help_text="Fecha y hora de la hora extra")

    semanal = [
        ('42', '42 Horas'),
        ('43', '43 Horas'),
        ('44', '44 Horas'),
        ('45', '45 Horas'),
        ('46', '46 Horas'),
        ('47', '47 Horas'),
        ]

    horas_Semanales = models.CharField(max_length=3, choices=semanal,blank=True, null=True, help_text="Horas semanales Trbajadas")
    
    tipo_Hora = models.ForeignKey(TipoHoraRecargo,on_delete=models.CASCADE, null=True)
    
    horas_trabajadas = models.DecimalField(max_digits=5,blank=True, null=True, decimal_places=2, help_text="Número de horas trabajadas")
    valor = models.DecimalField(max_digits=10,blank=True, null=True, decimal_places=2, help_text="Valor de las horas trabajadas")

    def __str__(self):
        return f"{self.fecha_hora} - {self.horas_trabajadas} horas - {self.valor} valor"
