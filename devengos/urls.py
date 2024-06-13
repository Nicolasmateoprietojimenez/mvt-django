from django.urls import path
from . import views

urlpatterns = [
    path('',views.listarHoras, name='horas'),
    path('calcular/<int:nro_documento>/', views.calcularHoras,name='calcula'),
    path('registrarHoras/', views.registrarHoras, name='nuevo_Horo'),
    path('buscar/', views.buscar_empleado, name='buscar_empleado'),
]