# deducciones/views.py

from django.shortcuts import render, get_object_or_404, redirect
from gestion_empleados.models import Empleado as GestionEmpleado
from .models import Prima
from .forms import PrimaForm

def detalle_prima(request, prima_id):
    prima = get_object_or_404(Prima, id=prima_id)

    data = {
        'prima': prima,
    }
    return render(request, 'deducciones/detalle_prima.html', data)

def calcular_seguridad_social(request, empleado_nro_documento):
    empleado = get_object_or_404(GestionEmpleado, nro_documento=empleado_nro_documento)
    salario_base = empleado.salario_base
    salud_descuento = salario_base * 0.04
    pension_descuento = salario_base * 0.04
    salario_final = salario_base - (salud_descuento + pension_descuento)

    data = {
        'empleado': empleado,
        'salario_base': salario_base,
        'salud_descuento': salud_descuento,
        'pension_descuento': pension_descuento,
        'salario_final': salario_final,
    }
    
    return render(request, 'deducciones/calcular_seguridad_social.html', data)

def registrar_prima(request, empleado_nro_documento):
    empleado = get_object_or_404(GestionEmpleado, nro_documento=empleado_nro_documento)
    
    if request.method == 'POST':
        form = PrimaForm(request.POST)
        if form.is_valid():
            dias_trabajados = form.cleaned_data['dias_trabajados']
            prima_calculada = empleado.salario_base * dias_trabajados / 360

            prima = form.save(commit=False)
            prima.empleado = empleado
            prima.prima_calculada = prima_calculada
            prima.save()

            # Calcular el total
            total = empleado.salario_base + prima_calculada

            return render(request, 'deducciones/registrar_prima.html', {'form': form, 'empleado': empleado, 'salario_base': empleado.salario_base, 'prima_calculada': prima_calculada, 'total': total})

    else:
        form = PrimaForm()

    return render(request, 'deducciones/registrar_prima.html', {'form': form, 'empleado': empleado, 'salario_base': empleado.salario_base})


from decimal import Decimal

def calcular_arl(request, empleado_nro_documento):
    empleado = get_object_or_404(GestionEmpleado, nro_documento=empleado_nro_documento)
    nivel_riesgo = empleado.nivel_riesgo
    porcentaje_nivel = nivel_riesgo.porcentaje_nivel

    salario_base = empleado.salario_base
    valor_arl = (Decimal(salario_base) * Decimal('0.4')) * (porcentaje_nivel / Decimal('100'))

    data = {
        'empleado': empleado,
        'nivel_riesgo': nivel_riesgo,
        'porcentaje_nivel': porcentaje_nivel,
        'valor_arl': valor_arl,
    }

    return render(request, 'deducciones/arl.html', data)
