from django.db import models

# Create your models here.

class Medicos(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'
      