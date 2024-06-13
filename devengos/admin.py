from django.contrib import admin

# Register your models here.

from .models import HoraExtra, TipoHoraRecargo

admin.site.register(HoraExtra)
admin.site.register(TipoHoraRecargo)