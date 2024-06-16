from django.shortcuts import render
from gestion_empleados.models import Empleado


def home_empleados(request, empleado_nro_documento):
    empleado = Empleado.objects.get(nro_documento=empleado_nro_documento)
    return render(request, 'home_empleados.html', {'empleado': empleado, 'registros': empleado})