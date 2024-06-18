from django.shortcuts import render, get_object_or_404

from login.models import Administrador
from .models import Empleado

def home_empleados(request, empleado_nro_documento, rol):
    if rol == 'GESTOR':
        empleado = get_object_or_404(Administrador, pk=empleado_nro_documento)
    else:
        empleado = get_object_or_404(Empleado, pk=empleado_nro_documento)
    data = {
        'nro_documento': empleado.nro_documento,
        'rol': rol,
        'nombre1': empleado.nombre1,
        'nombre2': empleado.nombre2,
    }
    
    return render(request, 'home_empleados.html', data)
