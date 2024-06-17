# deducciones/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('seguridad_social/<int:empleado_nro_documento>/', views.calcular_seguridad_social, name='calcular_seguridad_social'),
    path('registrar_prima/<int:empleado_nro_documento>/', views.registrar_prima, name='registrar_prima'),
    path('detalle_prima/<int:prima_id>/', views.detalle_prima, name='detalle_prima'), 
    path('calcular_arl/<str:empleado_nro_documento>/', views.calcular_arl, name='calcular_arl'),

]
