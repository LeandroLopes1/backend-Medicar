# Generated by Django 4.0.4 on 2022-04-18 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0002_rename_id_medico_medicos_id_alter_medicos_crm'),
        ('agendas', '0013_alter_agendas_dia'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='agendas',
            unique_together={('dia', 'horario', 'medico')},
        ),
    ]