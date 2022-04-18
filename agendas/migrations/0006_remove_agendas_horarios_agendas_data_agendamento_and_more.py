# Generated by Django 4.0.4 on 2022-04-18 20:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendas', '0005_alter_agendas_horarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendas',
            name='horarios',
        ),
        migrations.AddField(
            model_name='agendas',
            name='data_agendamento',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='agendas',
            name='horario',
            field=models.TimeField(choices=[('08:00', '08:00'), ('09:00', '09:00'), ('10:00', '10:00')], default=datetime.time(8, 0)),
        ),
    ]