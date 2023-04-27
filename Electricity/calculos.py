from django.db.models import Sum,Avg,Max,Min,Count
from datetime import datetime, timezone, timedelta
from .models import Medida, Inversor

DIA = 'dia'
SEMANA = 'semana'
MES = 'mes'

def energia(data,inversor=False):

    now = datetime.now(timezone.utc)

    print(data)

    if data == DIA:
        filter_kwargs  = {
            'created__year':now.year,
            'created__month':now.month,
            'created__day':now.day 
            }
        
    elif data == SEMANA:
        filter_kwargs = {
            'created__year': now.year,
            'created__month': now.month,
            'created__week_day': now.weekday() + 1,
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

    return Medida.objects.filter(**filter_kwargs).aggregate(Sum('potenciav2'))['potenciav2__sum']