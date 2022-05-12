from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from consultas.api.serializers import ConsultasSerializer
from consultas.models import Consultas
from consultas.api.serializers import ConsultaDetalhesSerializer


class ConsultasViewSet(viewsets.ModelViewSet):
    queryset = Consultas.objects.all()
    serializer_class = ConsultasSerializer
    filterset_fields = ('crm', 'dia', 'horario')

    @action(detail=True, methods=['get'])
    def listar_consultas(self, request, pk=None):
        consultas = Consultas.objects.filter(medico=pk)
        serializer = ConsultaDetalhesSerializer(consultas, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def marcar_consulta(self, request, pk=None):
        consulta = Consultas.objects.get(id=pk)
        consulta.marcada = True
        consulta.save()
        return Response(status=200)