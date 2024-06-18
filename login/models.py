from django.utils import timezone
from django.db import models


# Create your models here.



class Administrador(models.Model):
        
    # Datos de logeo y verificación de registro
    TIPO_DOCUMENTO_CHOICES = (
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('PSP', 'Pasaporte'),
    )
    tipo_documento = models.CharField(max_length=20, choices=TIPO_DOCUMENTO_CHOICES)
    nro_documento = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=100)
    correo = models.EmailField()

    nombre1 = models.CharField(max_length=255)
    nombre2 = models.CharField(max_length=255, blank=True, null=True)
    apellido1 = models.CharField(max_length=255)
    apellido2 = models.CharField(max_length=255, blank=True, null=True)
    numero_celular = models.CharField(max_length=20, blank=True, null=True)

    estado_cuenta = models.BooleanField(default=False)  # Toda cuenta creada deberá ser activada por medio de correo electrónico
    # Campos específicos de los roles operador y lector
    
    
    def __str__(self):
        return f"{self.nro_documento}"

class TokenAccess(models.Model):
    usuario = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    token = models.CharField(max_length=6)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Token {self.token} para {self.usuario}"
    