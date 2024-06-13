from django.shortcuts import render,redirect
from django.db.models import Sum
from gestion_empleados.models import Empleado
from . models import TipoHoraRecargo, HoraExtra
from .forms import TipoHoraRecargoform, HoraExtraform, BuscarEmpleadoForm


# Create your views here.

def deveng(request):
    return render(request,'homeDevengado.html')
    
def listarHoras(request):
    horas = HoraExtra.objects.all()
    return render(request, 'horas.html',{'horas': horas})

def registrarHoras(request):
    formulario = HoraExtraform(request.POST, request.FILES)
    if formulario.is_valid():
        formulario.save()
        return redirect('horas') 
    return render(request, 'registro_horas.html', {"form": formulario, "mensaje": "ok"})

def calcularHoras(request, nro_documento):
    usuario = Empleado.objects.get(pk=nro_documento)
    horas_extras = HoraExtra.objects.filter(nro_documento=usuario)
    
    salario = usuario.salario_base
    nombre = usuario.nombre1
    apellido = usuario.apellido1
     
    # Iterar sobre cada objeto HoraExtra encontrado
    for horitas in horas_extras:
        fecha_hora = horitas.fecha_hora
        tipo_horas = horitas.tipo_Hora.tipo_hora_recargo
        horasSemanal = int(horitas.horas_Semanales)
        hora1 = int(horitas.horas_trabajadas)

        calculo = salario / horasSemanal
        resultado = 0

        if tipo_horas == 'extra_diurno':
            resultado = (calculo * 0.25) * hora1  # extra diurna
        elif tipo_horas == 'extra_nocturno':
            resultado = (calculo * 0.75) * hora1  # extra nocturna
        elif tipo_horas == 'extra_diurno_dominical_festivo':
            resultado = (calculo + calculo) * hora1  # extra diurna dominical
        elif tipo_horas == 'extra_nocturno_dominical_festivo':
            resultado = (calculo * 1.50) * hora1  # extra nocturna dominical
        elif tipo_horas == 'recargo_nocturno': 
            resultado = (calculo * 0.35) * hora1  # recargo nocturno
        elif tipo_horas == 'recargo_dominical_festivo':
            resultado = (calculo * 0.75) * hora1  # recargo dominical
        elif tipo_horas == 'recargo_nocturno_dominical_festivo':
            resultado = (calculo * 1.10) * hora1  # recargo nocturno dominical

        
        horitas.valor = resultado
        horitas.save()

        data = {
            'nombre': nombre,
            'apellido': apellido,
            'resultado': resultado,
            'horasSemanal':horasSemanal,
            'fecha_hora':fecha_hora,
            'hora1':hora1,
            'tipo_horas':tipo_horas,
        }
    
    return render(request, 'calculo.html', data)


def buscar_empleado(request):
    empleado = None
    horas_extras = None
    total_valor = 0
    salario_total = 0
    if request.method == 'POST':
        form = BuscarEmpleadoForm(request.POST)
        if form.is_valid():
            nro_documento = form.cleaned_data['nro_documento']
            empleado = Empleado.objects.get(nro_documento=nro_documento)
            horas_extras = HoraExtra.objects.filter(nro_documento=empleado)
            total_valor = sum(horas_extras.values_list('valor', flat=True))
            salario_total = total_valor + empleado.salario_base
    else:
        form = BuscarEmpleadoForm()

    return render(request, 'buscar.html', {
        'form': form,
        'empleado': empleado,
        'horas_extras': horas_extras,
        'total_valor':total_valor,
        'salario_total':salario_total,
    })
