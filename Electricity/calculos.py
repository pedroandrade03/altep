from django.db.models import Sum,Avg,Max,Min,Count
from datetime import datetime, timezone, timedelta
from .models import Medida, Inversor

DIA     = 'dia'
SEMANA  = 'semana'
MES     = 'mes'
MEDIDA  = 1000

def energia(data,inversor=False):

    now = datetime.now(timezone.utc)

    if data == DIA:
        filter_kwargs  = {
            'created__year':now.year,
            'created__month':now.month,
            'created__day':now.day 
            }
        
    elif data == SEMANA:
        filter_kwargs = {
            'created__gte': (now - timedelta(days=now.weekday()+1)),
            'created__lte': (now - timedelta(days=now.weekday()+1)) + timedelta(days=6)	
        }

    elif data == MES:
        filter_kwargs = {
            'created__year': now.year,
            'created__month': now.month,
        }
    else:
        raise ValueError(f"Invalid value for 'data': {data}")
    
    if inversor:
        inversor = Inversor.objects.get(number=inversor)
        filter_kwargs ['painel'] = inversor
    
    return (Medida.objects.filter(**filter_kwargs).aggregate(Sum('potenciav2'))['potenciav2__sum'] or 0) / MEDIDA

def energia_grafico(data,inversor):

    now = datetime.now(timezone.utc)

    inversor = Inversor.objects.get(number=inversor)

    list_grafic = []

    if data == DIA:
        
        filter_kwargs  = {
            'created__year':now.year,
            'created__month':now.month,
            'created__day':now.day 
        }
        
        for hour in range(0, 22, 3):
            filter_kwargs['created__hour'] = hour
            medida = Medida.objects.filter(**filter_kwargs).filter(painel=inversor).last()

            if medida == None:  
                medida = 0
            else:
                medida = medida.potenciav2 / MEDIDA

            list_grafic.append(medida)

        return list_grafic
    
    if data == SEMANA:

        filter_kwargs = {}
        for day in range(0, 7):
            dia_semana           = (now - timedelta(days=now.weekday() + 1)) + timedelta(days=day)
            dia_da_semana_inicio = dia_semana.replace(hour=0, minute=0, second=0, microsecond=0)
            dia_da_semana_final  = dia_da_semana_inicio + timedelta(hours=23,minutes=59,seconds=59)

            filter_kwargs['created__gte'] = dia_da_semana_inicio
            filter_kwargs['created__lte'] = dia_da_semana_final

            medida = (Medida.objects.filter(**filter_kwargs).filter(painel=inversor).aggregate(Sum('potenciav2'))['potenciav2__sum'] or 0) / MEDIDA

            list_grafic.append(medida)

        return list_grafic


def inversor(inversor):

    inversor = Inversor.objects.get(number=inversor)

    medida = Medida.objects.filter(painel=inversor).last()

    if medida == None:  
        medida = 0
    else:
        medida = medida.potenciav2 / MEDIDA

    return medida

            
    