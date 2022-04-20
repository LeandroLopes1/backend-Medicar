from datetime import datetime, time
from django.db import models

from medicos.models import Medicos
from agendas.models import Agendas

# Create your models here.

class Consultas(models.Model):
    dia = models.DateField(default=datetime.now)
    HORARIOS_CHOICES = (
        (time(8,0,0), '8:00:00'),
        (time(8,30,0), '8:30:00'),
        (time(9,0,0), '9:00:00'),
        (time(9,30,0), '9:30:00'),
        (time(10,0,0), '10:00:00'),
    )
    horario = models.TimeField(choices=HORARIOS_CHOICES, default=time(8, 0))
    data_agendamento = models.DateTimeField(auto_now_add=True)
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE, related_name='consultas', blank=False, null=False)
    agenda = models.ForeignKey(Agendas, on_delete=models.CASCADE, related_name='consultas', blank=False, null=False)

    def __str__(self):
        return self.medico.nome

    class Meta:
        managed = True
        db_table = 'consultas'
        unique_together = (('dia', 'horario', 'medico'),)