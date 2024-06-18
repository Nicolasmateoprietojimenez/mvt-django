import string
from django.shortcuts import render, redirect

from gestion_empleados.models import Empleado
from login.forms import AdminForm, LoginForm, TokenVerificationForm

from django.utils.crypto import get_random_string
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from login.models import Administrador, TokenAccess


def enviar_correo(correo_destinatario, token):
    subject = 'Bienvenido a NomiGo'
    from_email = settings.EMAIL_HOST_USER
    to_email = [correo_destinatario]

    html_content = render_to_string('correo_bienvenida.html', {'token': token})
    msg = EmailMultiAlternatives(subject, strip_tags(html_content), from_email, to_email)
    msg.attach_alternative(html_content, "text/html")

    msg.send()


def crear_cuenta(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            empleado = form.save()
            token = get_random_string(length=6, allowed_chars=string.digits)
            enviar_correo(correo_destinatario=empleado.correo, token=token)
            TokenAccess.objects.create(usuario=empleado, token=token)
            return redirect('success')
    else:
        form = AdminForm()
    return render(request, 'register.html', {'form': form})

def verificar_token(request):
    mensaje = None

    if request.method == 'POST':
        form = TokenVerificationForm(request.POST)
        if form.is_valid():
            nro_documento = form.cleaned_data['nro_documento']
            token = form.cleaned_data['token']
            
            try:
                usuario =Administrador.objects.get(nro_documento=nro_documento)
                token_reciente = TokenAccess.objects.filter(usuario=usuario).latest('fecha_creacion')
                
                if token == token_reciente.token:
                    usuario.estado_cuenta = True
                    usuario.save()
                    token_reciente.delete()
                    mensaje = f"¡Token verificado correctamente para el usuario {usuario.nro_documento}!"
                else:
                    mensaje = "El token ingresado no es válido."
            
            except Empleado.DoesNotExist:
                mensaje = "El número de documento no existe."
            except TokenAccess.DoesNotExist:
                mensaje = "No hay tokens registrados para este usuario."

    else:
        form = TokenVerificationForm()

    return render(request, 'verificar_token.html', {'form': form, 'mensaje': mensaje})


def success(request):
    return render(request, 'success.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            tipo_documento = form.cleaned_data['tipo_documento']
            nro_documento = form.cleaned_data['nro_documento']
            password = form.cleaned_data['password']
            
            empleado = None
            administrador = None
            
            try:
                empleado = Empleado.objects.get(tipo_documento=tipo_documento, nro_documento=nro_documento)
                if password == empleado.password:
                    if empleado.estado_cuenta:
                        request.session['empleado_nro_documento'] = empleado.nro_documento
                        request.session['empleado_rol'] = empleado.rol
                        return redirect('home_empleados', empleado_nro_documento=empleado.nro_documento, rol=empleado.rol)
                    else:
                        form.add_error(None, "La cuenta no está activada.")
                else:
                    form.add_error('password', "Contraseña incorrecta.")
            except Empleado.DoesNotExist:
                try:
                    administrador = Administrador.objects.get(tipo_documento=tipo_documento, nro_documento=nro_documento)
                    if password == administrador.password:
                        if administrador.estado_cuenta:
                            request.session['empleado_nro_documento'] = administrador.nro_documento
                            request.session['empleado_rol'] = 'GESTOR'
                            return redirect('home_empleados', empleado_nro_documento=administrador.nro_documento, rol=request.session['empleado_rol'])

                        else:
                            form.add_error(None, "La cuenta no está activada.")
                    else:
                        form.add_error('password', "Contraseña incorrecta.")
                except Administrador.DoesNotExist:
                    form.add_error('nro_documento', "El documento no está registrado.")
    else:
        form = LoginForm()

    return render(request, 'login_empleado.html', {'form': form})