from datetime import datetime
from django.db import models
from medicos.models import Medicos
from datetime import datetime, time

# Create your models here.

class Agendas(models.Model):
    dia =  models.DateField(default=datetime.now)
    HORARIOS_CHOICES = (
        (time(8,0,0), '8:00:00'),
        (time(8,30,0), '8:30:00'),
        (time(9,0,0), '9:00:00'),
        (time(9,30,0), '9:30:00'),
        (time(10,0,0), '10:00:00'),
    )
    horario = models.TimeField(choices=HORARIOS_CHOICES, default=time(8, 0))
 
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE, related_name='agendas', blank=False, null=False)

    def __str__(self):
        return self.medico.nome

    class Meta:
        managed = True
        db_table = 'agendas'
        unique_together = (('dia', 'horario', 'medico'),)

