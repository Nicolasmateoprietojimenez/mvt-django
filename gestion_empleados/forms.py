from django import forms

class LoginForm(forms.Form):
    tipo_documento = forms.ChoiceField(choices=[
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('PSP', 'Pasaporte'),
        ('RC', 'Registro Civil'),
    ])
    nro_documento = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)