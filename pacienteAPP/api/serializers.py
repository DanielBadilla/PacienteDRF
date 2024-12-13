from rest_framework import serializers
from pacienteAPP.models import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'rut', 'apellidos', 'nombres', 'diagnostico', 'doctor', 'fecha_consulta', 'hora_consulta']
