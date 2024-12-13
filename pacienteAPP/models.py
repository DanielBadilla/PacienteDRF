
from django.db import models

class Paciente(models.Model):
    # Atributos básicos
    rut = models.CharField(max_length=12, unique=True)  # RUT del paciente
    apellidos = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)

    # Atributos adicionales
    diagnostico = models.CharField(max_length=255)
    doctor = models.CharField(max_length=100)  # Doctor que atendió al paciente
    fecha_consulta = models.DateField()  # Fecha de consulta
    hora_consulta = models.TimeField()  # Hora de consulta

    # Atributos automáticos
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nombres} {self.apellidos} ({self.rut})'
