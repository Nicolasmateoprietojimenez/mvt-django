from django import views
from django.urls import path

from gestion_empleados.views import login_view
from gestion_empleados.views import home_empleados

urlpatterns = [
    path('login/', login_view, name='login'),
        path('empleados/<str:empleado_nro_documento>/', home_empleados, name='home_empleados'),

]