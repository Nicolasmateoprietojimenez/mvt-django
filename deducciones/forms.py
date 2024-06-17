
from django import forms
from .models import Prima

class PrimaForm(forms.ModelForm):
    class Meta:
        model = Prima
        fields = ['dias_trabajados']
