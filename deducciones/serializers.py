from rest_framework import serializers
from .models import Prima, SeguridadSocial, NivelRiesgo, Empleado

class PrimaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prima
        fields = '__all__'  

class SeguridadSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeguridadSocial
        fields = '__all__'

class NivelRiesgoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelRiesgo
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'
