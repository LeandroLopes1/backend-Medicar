from rest_framework import serializers

from consultas.models import Consultas
from medicos.api.serializers import MedicosSerializer
from agendas.api.serializers import RegistroHorariosSerializer


class ConsultasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultas
        fields = ('id', 'dia', 'horario', 'medico', 'agenda', 'data_agendamento')
        read_only_fields = ('data_agendamento',)

class ConsultaDetalhesSerializer(ConsultasSerializer):
    medico = MedicosSerializer(read_only=True)
    horario = RegistroHorariosSerializer(read_only=True)
    
    class Meta(ConsultasSerializer.Meta):
        fields = [
            'id',
            'dia',
            'horario',
            'data_agendamento',
            'medico',       
         ]

