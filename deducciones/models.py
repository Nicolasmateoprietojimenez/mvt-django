from django.db import models
from django.db import models
from gestion_empleados.models import Empleado as GestionEmpleado
from django.db import models
from gestion_empleados.models import Empleado

class Prima(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    dias_trabajados = models.IntegerField()
    prima_calculada = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.prima_calculada = self.empleado.salario_base * self.dias_trabajados / 360
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.empleado} - Prima"


class SeguridadSocial(models.Model):
    empleado = models.OneToOneField(
        GestionEmpleado,
        on_delete=models.CASCADE,
        related_name='seguridad_social'  # Nombre relacionado para acceder desde Empleado
    )

    CONCEPTO_CHOICES = [
        ('salud_empleador', 'Salud Empleador'),
        ('salud_empleado', 'Salud Empleado'),
        ('pension_empleador', 'Pensión Empleador'),
        ('pension_empleado', 'Pensión Empleado'),
    ]

    concepto = models.CharField(max_length=20, choices=CONCEPTO_CHOICES)
    porcentaje_seguridad_social = models.DecimalField(max_digits=5, decimal_places=2, help_text="Porcentaje de SS")

    def __str__(self):
        return f"{self.empleado} - {self.concepto} - {self.porcentaje_seguridad_social}%"


class NivelRiesgo(models.Model):
    nivel_riesgo = models.CharField(max_length=100, help_text="Nivel de riesgo", choices=[
        ('1', 'Riesgo I'),
        ('2', 'Riesgo II'),
        ('3', 'Riesgo III'),
        ('4', 'Riesgo IV'),
        ('5', 'Riesgo V'),
    ])
    porcentaje_nivel = models.DecimalField(max_digits=5, decimal_places=2, help_text="Porcentaje del nivel de riesgo")

    def __str__(self):
        return f"{self.get_nivel_riesgo_display()} - {self.porcentaje_nivel}%"
