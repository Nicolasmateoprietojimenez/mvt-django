# deducciones/api_views.py

from decimal import Decimal
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from gestion_empleados.models import Empleado
from .models import Prima, SeguridadSocial, NivelRiesgo
from .serializers import PrimaSerializer, SeguridadSocialSerializer, NivelRiesgoSerializer, EmpleadoSerializer

class PrimaViewSet(viewsets.ModelViewSet):
    queryset = Prima.objects.all()
    serializer_class = PrimaSerializer

    @action(detail=True, methods=['get'])
    def calcular_prima(self, request, pk=None):
        prima = self.get_object()
        prima_calculada = prima.empleado.salario_base * prima.dias_trabajados / 360
        return Response({'prima_calculada': prima_calculada})


class SeguridadSocialViewSet(viewsets.ModelViewSet):
    queryset = SeguridadSocial.objects.all()
    serializer_class = SeguridadSocialSerializer

    @action(detail=True, methods=['get'])
    def calcular_seguridad_social(self, request, pk=None):
        empleado = get_object_or_404(Empleado, nro_documento=pk)
        salud_descuento = empleado.salario_base * Decimal('0.04')
        pension_descuento = empleado.salario_base * Decimal('0.04')
        salario_final = empleado.salario_base - (salud_descuento + pension_descuento)
        
        return Response({
            'salud_descuento': salud_descuento,
            'pension_descuento': pension_descuento,
            'salario_final': salario_final,
        })


class NivelRiesgoViewSet(viewsets.ModelViewSet):
    queryset = NivelRiesgo.objects.all()
    serializer_class = NivelRiesgoSerializer

    @action(detail=True, methods=['get'])
    def calcular_arl(self, request, pk=None):
        empleado = get_object_or_404(Empleado, nro_documento=pk)
        porcentaje_nivel = empleado.nivel_riesgo.porcentaje_nivel
        salario_base = empleado.salario_base
        valor_arl = (salario_base * Decimal('0.4')) * (porcentaje_nivel / Decimal('100'))
        return Response({'valor_arl': valor_arl })


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

    def retrieve(self, request, pk=None):
        empleado = get_object_or_404(self.queryset, nro_documento=pk)
        serializer = self.serializer_class(empleado)
        return Response(serializer.data)