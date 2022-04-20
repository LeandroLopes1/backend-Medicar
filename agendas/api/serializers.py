from rest_framework import serializers

from agendas.models import Agendas, RegistroHorarios
from medicos.api.serializers import MedicosSerializer

class RegistroHorariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroHorarios
        fields = ('hora',)

class AgendasSerializer(serializers.ModelSerializer):
    medico = MedicosSerializer()
    agendas = RegistroHorariosSerializer(many=True)

    class Meta:
        model = Agendas
        fields = ('id', 'medico', 'dia', 'agendas')