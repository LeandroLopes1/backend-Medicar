# Generated by Django 4.0.4 on 2022-04-18 20:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0002_rename_id_medico_medicos_id_alter_medicos_crm'),
        ('agendas', '0002_alter_horarios_agenda'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agendas',
            options={'managed': True},
        ),
        migrations.AddField(
            model_name='agendas',
            name='horarios',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='agendas',
            name='dia',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterUniqueTogether(
            name='agendas',
            unique_together={('medico', 'dia')},
        ),
        migrations.AlterModelTable(
            name='agendas',
            table='agendas',
        ),
        migrations.DeleteModel(
            name='Horarios',
        ),
    ]
