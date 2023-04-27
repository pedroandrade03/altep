from django.contrib import admin
from . models import Medida, Inversor

class MedidaAdmin(admin.ModelAdmin):
    list_display = ('painel','created','potenciav2','power_led','solarnet_led','solarweb_led')
    list_filter  = ("painel",)

class InversorAdmin(admin.ModelAdmin):
    list_display = ('name','number')

admin.site.register(Medida,MedidaAdmin)
admin.site.register(Inversor,InversorAdmin)
