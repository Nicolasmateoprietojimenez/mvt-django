import re
from django import forms
from gestion_empleados.models import Empleado

class LoginForm(forms.Form):
    tipo_documento = forms.ChoiceField(choices=[
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('PSP', 'Pasaporte'),
        ('RC', 'Registro Civil'),
    ], widget=forms.Select(attrs={'placeholder': 'Selecciona un tipo de documento'}))

    nro_documento = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Ej: 100364578'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

    
class EmpleadoForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(), 
        label="Contraseña",
    )
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirmar Contraseña")
    
    class Meta:
        model = Empleado
        fields = [
            'tipo_documento',
            'nro_documento',
            'fecha_expedicion',
            'nombre1',
            'nombre2',
            'apellido1',
            'apellido2',
            'numero_celular',
            'correo',
            'password',
        ]
        widgets = {
            'fecha_expedicion': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_nro_documento(self):
        nro_documento = self.cleaned_data.get("nro_documento")
        if not nro_documento.isdigit():
            raise forms.ValidationError("El número de documento debe contener solo dígitos.")
        if len(nro_documento) > 10:
            raise forms.ValidationError("El número de documento no puede tener más de 10 dígitos.")
        return nro_documento

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not re.search(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$', password):
            raise forms.ValidationError(
                "La contraseña debe tener entre 8 y 16 caracteres, incluir al menos una letra mayúscula, un número y un símbolo."
            )
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden")

        return cleaned_data

class TokenVerificationForm(forms.Form):
    nro_documento = forms.CharField(label="Número de Documento")
    token = forms.CharField(label="Token")