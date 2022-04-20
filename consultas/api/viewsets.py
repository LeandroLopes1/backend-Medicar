from rest_framework import viewsets

from consultas.api.serializers import ConsultasSerializer
from consultas.models import Consultas


class ConsultasViewSet(viewsets.ModelViewSet):
    queryset = Consultas.objects.all()
    serializer_class = ConsultasSerializer
