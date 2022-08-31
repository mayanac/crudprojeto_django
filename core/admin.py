from django.contrib import admin
from .models import Marmita

@admin.register(Marmita)
class MarmitaAdmin(admin.ModelAdmin):
    list_display= ['id', 'sabor','descricao','user']

