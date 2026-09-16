from django.contrib import admin
from agendamento import models

@admin.register(models.Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = 'id', 'date', 'tittle', 'created_at',
    ordering = 'date',
    list_filter = 'created_at',
    search_fields = 'date', 'tittle', 'created_at'

    list_per_page = 1
    list_max_show_all = 50
    list_editable  = 'tittle', 'date',
    list_display_links = 'id', 'created_at',