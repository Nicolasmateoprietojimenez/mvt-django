def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            tipo_documento = form.cleaned_data['tipo_documento']
            nro_documento = form.cleaned_data['nro_documento']
            password = form.cleaned_data['password']
            
            try:
                empleado = Empleado.objects.get(tipo_documento=tipo_documento, nro_documento=nro_documento)
                if password == empleado.password:
                    if empleado.estado_cuenta:
                        request.session['empleado_nro_documento'] = empleado.nro_documento
                        request.session['empleado_rol'] = empleado.rol

                        return redirect('home_empleados', empleado_nro_documento=empleado.nro_documento)
                    else:
                        form.add_error(None, "La cuenta no está activada.")
                else:
                    form.add_error('password', "Contraseña incorrecta.")
            except Empleado.DoesNotExist:
                form.add_error('nro_documento', "El documento no está registrado.")
    else:
        form = LoginForm()

    return render(request, 'login_empleado.html', {'form': form})