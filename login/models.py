from django.utils import timezone
from django.db import models

from gestion_empleados.models import Empleado

# Create your models here.

class TokenAccess(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    token = models.CharField(max_length=6)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Token {self.token} para {self.empleado.nro_documento}"