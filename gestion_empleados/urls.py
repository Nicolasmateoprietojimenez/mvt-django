# gestion_empleados/urls.py

from django.urls import path
from .views import home_empleados

urlpatterns = [
<<<<<<< HEAD
    path('<int:empleado_nro_documento>/', home_empleados, name='home_empleados'),
=======
    path('home_empleados/<int:empleado_nro_documento>/', views.home_empleados, name='home_empleados'),
>>>>>>> origin/johan
]
