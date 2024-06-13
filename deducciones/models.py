from django.db import models

# Create your models here.

def empleadoDocu():
    from gestion_empleados.models import Empleado
    return Empleado

class SeguridadSocial(models.Model):

    nro_documento = models.ForeignKey('gestion_empleados.Empleado', on_delete=models.CASCADE, null=True)

    CONCEPTO_CHOICES = [
        ('salud_empleador', 'Salud Empleador'),
        ('salud_empleado', 'Salud Empleado'),
        ('pension_empleador', 'Pensión Empleador'),
        ('pension_empleado', 'Pensión Empleado'),
    ]

    concepto = models.CharField(max_length=20, choices=CONCEPTO_CHOICES)
    porcentaje_seguridad_social = models.DecimalField(max_digits=5, decimal_places=2, help_text="Porcentaje de SS")

    def __str__(self):
        return f"{self.concepto} - {self.porcentaje_seguridad_social}%"

arls = [
        ('1', 'Riesgo I'),
        ('2', 'Riesgo II'),
        ('3', 'Riesgo III'),
        ('4', 'Riesgo IV'),
        ('5', 'Riesgo V'),
    ]
porcen = [
        ('1', '0,348%'),
        ('2', '0,522%'),
        ('3', '1,044%'),
        ('4', '2,436%'),
        ('5', '6,960%'),
    ]
class NivelRiesgo(models.Model):
    nivel_riesgo = models.CharField(max_length=100, help_text="Nivel de riesgo",choices=arls)
    porcentaje_nivel = models.CharField(max_length=100,choices=porcen, help_text="Porcentaje del nivel de riesgo")

    def __str__(self):
        return f"{self.nivel_riesgo} - {self.porcentaje_nivel}%"