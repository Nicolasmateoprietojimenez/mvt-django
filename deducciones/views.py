from django.shortcuts import render, get_object_or_404
from gestion_empleados.models import Empleado as GestionEmpleado

def calcular_seguridad_social(request, empleado_nro_documento):
    # Obtener el empleado usando el modelo de gestion_empleados
    empleado = get_object_or_404(GestionEmpleado, nro_documento=empleado_nro_documento)
    
    # Obtener el salario base del empleado
    salario_base = empleado.salario_base
    
    # Calcular los descuentos
    salud_descuento = salario_base * 0.04
    pension_descuento = salario_base * 0.04
    salario_final = salario_base - (salud_descuento + pension_descuento)
    
    # Preparar el contexto con los datos del empleado y los cálculos
    context = {
        'empleado': empleado,
        'salario_base': salario_base,
        'salud_descuento': salud_descuento,
        'pension_descuento': pension_descuento,
        'salario_final': salario_final,
    }
    
    # Renderizar el template con los datos
    return render(request, 'deducciones/calcular_seguridad_social.html', context)
