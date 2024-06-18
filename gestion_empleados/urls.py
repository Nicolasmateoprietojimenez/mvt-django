# gestion_empleados/urls.py

from django.urls import path
from .views import home_empleados

urlpatterns = [
    path('home_empleados/<str:empleado_nro_documento>/<str:rol>/', home_empleados, name='home_empleados'),
]
