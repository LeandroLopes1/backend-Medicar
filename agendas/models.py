from tabnanny import verbose
from django.core.exceptions import ValidationError
from django.db import models

from datetime import datetime

from medicos.models import Medicos


# Create your models here.

class RegistroHorarios(models.Model):
    hora = models.TimeField(unique=True)

    class Meta:
        verbose_name = 'Registro de Horario'
        verbose_name_plural = 'Registros de Horarios'

    def __str__(self):
        return self.hora.strftime('%H:%M')

class Agendas(models.Model): 
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    dia = models.DateField()
    agendas = models.ManyToManyField(RegistroHorarios)
    inserido_em = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'
        unique_together = ('medico', 'dia')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.dia < datetime.today().date():
            raise ValidationError('A data deve ser maior que a data atual')
        super().save(force_insert, force_update, using, update_fields)
           
    
    def __str__(self):
        return f'{self.medico}, no dia {self.dia.strftime("%d/%m/%Y")}'

