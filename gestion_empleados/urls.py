# gestion_empleados/urls.py

from django.urls import path
from .views import home_empleados
from . import views

urlpatterns = [
    path('home_empleados/<str:empleado_nro_documento>/<str:rol>/', home_empleados, name='home_empleados'),
    path('empleados/<str:nro_documento>/', views.EmpleadoDetalle.as_view(), name='empleado-detalle'),

]
