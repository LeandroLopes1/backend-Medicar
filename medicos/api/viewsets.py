from rest_framework import viewsets

from medicos.models import Medicos
from medicos.api.serializers import MedicosSerializer

class MedicosViewSet(viewsets.ModelViewSet):
    queryset = Medicos.objects.all()
    serializer_class = MedicosSerializer
