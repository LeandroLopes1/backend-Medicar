from datetime import datetime, time
from django.db import models

from medicos.models import Medicos
from agendas.models import Agendas, RegistroHorarios

# Create your models here.

class Consultas(models.Model):
    dia = models.DateField(default=datetime.now)

    horario = models.ForeignKey(RegistroHorarios, on_delete=models.CASCADE)
    data_agendamento = models.DateTimeField(auto_now_add=True)
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE, related_name='consultas', blank=False, null=False)
    agenda = models.ForeignKey(Agendas, on_delete=models.CASCADE, related_name='consultas', blank=False, null=False)

    def __str__(self):
        return self.medico.nome

    class Meta:
        managed = True
        db_table = 'consultas'
        unique_together = (('dia', 'horario', 'medico'),)
