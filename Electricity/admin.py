from django.contrib import admin
from . models import Medida, Inversor, Energia

class MedidaAdmin(admin.ModelAdmin):
    list_display = ('painel','created','potenciav2','power_led','solarnet_led','solarweb_led')
    list_filter  = ("painel",)

class InversorAdmin(admin.ModelAdmin):
    list_display = ('name','number')

class EnergiaAdmin(admin.ModelAdmin):
    list_display = ('created','custo_por_kwh','ativo')

admin.site.register(Energia,EnergiaAdmin)
admin.site.register(Medida,MedidaAdmin)
admin.site.register(Inversor,InversorAdmin)
