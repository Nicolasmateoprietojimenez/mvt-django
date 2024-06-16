from django.urls import path
from . import views

urlpatterns = [
    path('home_empleados/<int:empleado_nro_documento>/', views.home_empleados, name='home_empleados'),
    # otras rutas
]
