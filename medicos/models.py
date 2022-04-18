import email
from django.db import models

# Create your models here.

class Medicos(models.Model):
    id_medico = models.AutoField(primary_key=True)
    crm = models.IntegerField()
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'medicos'