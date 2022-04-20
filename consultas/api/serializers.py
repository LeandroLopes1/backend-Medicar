from rest_framework import serializers

from consultas.models import Consultas

class ConsultasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultas
        fields = ('id', 'dia', 'horario', 'medico', 'agenda', 'data_agendamento')
        read_only_fields = ('data_agendamento',)
        