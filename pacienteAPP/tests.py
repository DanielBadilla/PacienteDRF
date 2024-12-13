from rest_framework.test import APITestCase
from rest_framework import status
from .models import Paciente

class PacienteTests(APITestCase):
    def test_crear_paciente(self):
        data = {
            'rut': '12345678-9',
            'apellidos': 'Pérez',
            'nombres': 'Juan',
            'diagnostico': 'Gripe',
            'doctor': 'Dr. Gómez',
            'fecha_consulta': '2024-12-01',
            'hora_consulta': '10:00:00'
        }
        response = self.client.post('/api/pacientes/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_filtrar_por_diagnostico(self):
        # Crear un paciente con un diagnóstico específico
        paciente = Paciente.objects.create(
            rut='12345678-9',
            apellidos='Pérez',
            nombres='Juan',
            diagnostico='Gripe',
            doctor='Dr. Gómez',
            fecha_consulta='2024-12-01',
            hora_consulta='10:00:00'
        )
        # Filtrar por diagnóstico
        response = self.client.get('/api/pacientes/filtrar_por_diagnostico/', {'diagnostico': 'gripe'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Debería devolver 1 paciente
