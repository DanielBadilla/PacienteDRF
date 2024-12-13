from rest_framework import viewsets
from pacienteAPP.models import Paciente
from pacienteAPP.api.serializers import PacienteSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    # Acción personalizada para filtrar por diagnóstico
    @action(detail=False, methods=['get'])
    def filtrar_por_diagnostico(self, request):
        diagnostico = request.query_params.get('diagnostico', None)
        if diagnostico:
            pacientes = Paciente.objects.filter(diagnostico__icontains=diagnostico)
            serializer = self.get_serializer(pacientes, many=True)
            return Response(serializer.data)
        return Response({'detail': 'Diagnóstico no proporcionado'}, status=status.HTTP_400_BAD_REQUEST)
