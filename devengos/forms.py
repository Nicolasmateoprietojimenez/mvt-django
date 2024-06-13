from django import forms
from . models import TipoHoraRecargo, HoraExtra

class TipoHoraRecargoform(forms.ModelForm):
    class Meta:
        model = TipoHoraRecargo
        fields = '__all__'

class HoraExtraform(forms.ModelForm):
    class Meta:
        model = HoraExtra
        fields = ["nro_documento","fecha_hora","horas_Semanales","tipo_Hora","horas_trabajadas"]

class BuscarEmpleadoForm(forms.Form):
    nro_documento = forms.CharField(label='Número de Documento', max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese el número de documento'
    }))