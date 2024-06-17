from django.urls import path
from . import views

urlpatterns = [
    path('calcular_seguridad_social/<str:empleado_nro_documento>/', views.calcular_seguridad_social, name='calcular_seguridad_social'),
]
