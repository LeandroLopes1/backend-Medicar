from datetime import datetime
from django.db import models
from medicos.models import Medicos
from datetime import datetime, time

# Create your models here.

class Agendas(models.Model):
    dia =  models.DateField(default=datetime.now)
    HORARIOS_CHOICES = (
        ('08:00', '08:00'),
        ('09:00', '09:00'),
        ('10:00', '10:00'),
    )
    horario = models.TimeField(choices=HORARIOS_CHOICES, default=time(8, 0))
    data_agendamento = models.DateTimeField(default=datetime.now, blank=True)
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE, related_name='agendas', blank=False, null=False)

    class Meta:
        managed = True
        db_table = 'agendas'
        unique_together = (('dia', 'horario', 'medico'),)

