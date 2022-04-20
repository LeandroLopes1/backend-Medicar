from django.contrib import admin

from medicos.models import Medicos

# Register your models here.

class MedicosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'email')
    list_display_links = ('nome', 'crm')
    search_fields = ('nome',)

admin.site.register(Medicos, MedicosAdmin)