from rest_framework import viewsets

from agendas.models import Agendas
from agendas.api.serializers import AgendasSerializer

class AgendasViewSet(viewsets.ModelViewSet):
    queryset = Agendas.objects.all().order_by('dia')
    serializer_class = AgendasSerializer

