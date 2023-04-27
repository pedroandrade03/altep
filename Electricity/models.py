from django.db import models

class Inversor(models.Model):
    name            = models.CharField(max_length=256, blank=True, null=True)
    local           = models.CharField(max_length=256, blank=True, null=True)
    number          = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return str(self.name)

class Medida(models.Model):

    created         = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    painel          = models.ForeignKey(Inversor, on_delete=models.CASCADE, blank=True, null=True)
    energia_diaV2   = models.FloatField(blank=True, null=True)
    energia_ano     = models.FloatField(blank=True, null=True)
    energia_total   = models.FloatField(blank=True, null=True)
    potenciav2      = models.FloatField(blank=True, null=True)
    power_led       = models.BooleanField(default=False)
    solarnet_led    = models.BooleanField(default=False)
    solarweb_led    = models.BooleanField(default=False)

    def __str__(self):
        return str(self.painel)
        