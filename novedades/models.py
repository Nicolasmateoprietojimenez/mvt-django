from django.db import models

# Create your models here.
from django.db import models

class Novedad(models.Model):
    VACACIONES = 'vacaciones'
    INCAPACIDAD = 'incapacidad'
    PERMISO = 'permiso'
    OTRO = 'otro'

    TIPOS_NOVEDAD_CHOICES = [
        (VACACIONES, 'Vacaciones'),
        (INCAPACIDAD, 'Incapacidad'),
        (PERMISO, 'Permiso'),
        (OTRO, 'Otro'),
    ]

    tipo_novedad = models.CharField(
        max_length=20,
        choices=TIPOS_NOVEDAD_CHOICES,
        help_text="Tipo de novedad"
    )
    fecha_inicio = models.DateField(help_text="Fecha de inicio")
    fecha_fin = models.DateField(help_text="Fecha de fin")
    monto = models.DecimalField(max_digits=10, decimal_places=2, help_text="Monto")

    def __str__(self):
        return f"{self.get_tipo_novedad_display()} - {self.monto}"
