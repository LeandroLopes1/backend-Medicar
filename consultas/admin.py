from atexit import register
from django.contrib import admin

# Register your models here.

from consultas.models import Consultas

# Register your models here.

class ConsultasAdmin(admin.ModelAdmin):
    list_display = ('id', 'dia', 'horario', 'medico', 'agenda', 'data_agendamento')
    list_display_links = ('id', 'dia')
    search_fields = ('id', 'dia', 'horario', 'medico', 'agenda', 'data_agendamento')

admin.site.register(Consultas, ConsultasAdmin)
