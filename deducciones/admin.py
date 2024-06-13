from django.contrib import admin

from deducciones.models import NivelRiesgo, SeguridadSocial



# Register your models here.

admin.site.register(SeguridadSocial)
admin.site.register(NivelRiesgo)