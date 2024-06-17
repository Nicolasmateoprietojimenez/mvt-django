# gestion_empleados/urls.py

from django.urls import path
from .views import home_empleados

urlpatterns = [
    path('<int:empleado_nro_documento>/', home_empleados, name='home_empleados'),
]
