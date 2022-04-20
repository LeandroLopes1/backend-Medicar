import email
from django.db import models

# Create your models here.

class Medicos(models.Model):
    id = models.AutoField(primary_key=True)
    crm = models.CharField(max_length=4)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        managed = True
        db_table = 'medicos'