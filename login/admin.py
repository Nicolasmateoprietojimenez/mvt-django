from django.contrib import admin

from login.models import TokenAccess, Administrador

# Register your models here.
admin.site.register(TokenAccess)
admin.site.register(Administrador)