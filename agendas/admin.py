from django.contrib import admin

from agendas.models import Agendas

# Register your models here.

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('dia', 'horario', 'medico')
    list_filter = ('dia', 'horario', 'medico')
    search_fields = ('dia', 'horario', 'medico')


admin.site.register(Agendas, AgendaAdmin)