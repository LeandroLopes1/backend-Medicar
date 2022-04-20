from rest_framework import serializers

from agendas.models import Agendas

class AgendasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendas
        fields = ('id', 'dia', 'horario', 'medico')
        read_only_fields = ('id',)