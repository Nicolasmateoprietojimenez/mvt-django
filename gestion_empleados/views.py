# gestion_empleados/views.py

from django.shortcuts import render, get_object_or_404
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from .models import Empleado
from .serializers import EmpleadoSerializer
from login.models import Administrador

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

class EmpleadoDetalle(RetrieveAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    lookup_field = 'nro_documento'  

    def retrieve(self, request, *args, **kwargs):

        empleado = get_object_or_404(self.queryset, nro_documento=kwargs['nro_documento'])
        serializer = self.serializer_class(empleado)
        return Response(serializer.data)
