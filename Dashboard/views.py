from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Electricity.models import Medida, Inversor
import  Electricity.calculos as calculos
from django.db.models.functions import TruncHour
from django.utils import timezone
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta


@login_required
def home(request):
    
    context = {}

    for inversor in range(1,5):
        context[f'inversor_{inversor}'], context[f'inversor_{inversor}_status'], context[f'inversor_{inversor}_percent'],context[f'inversor_{inversor}_variation'], context[f'inversor_{inversor}_last_activity'] = calculos.inversor(inversor)
        context[f'inversor_{inversor}_energia_dia_grafico']    = calculos.energia_grafico('dia',inversor)
        context[f'inversor_{inversor}_energia_semana_grafico'] = calculos.energia_grafico('semana',inversor)
        context[f'inversor_{inversor}_energia_mes_grafico']    = calculos.energia_grafico('mes',inversor)

    context['energia_dia_economia_grafico']     = calculos.economia_grafico('dia')
    context['energia_semana_economia_grafico']  = calculos.economia_grafico('semana')
    context['energia_mes_economia_grafico']     = calculos.economia_grafico('mes')

    context['energia_dia_total']     = calculos.energia('dia')
    context['energia_semana_total']  = calculos.energia('semana')
    context['energia_mes_total']     = calculos.energia('mes')

    return render(request, 'dashboard/index.html', context)

def handler400(request, exception):
    return render(request, 'error/error-maintenance.html')

def handler403(request, exception):
    return render(request, 'error/error-404.html')

def handler404(request, exception):
    return render(request, 'error/error-404.html')

def handler500(request):
    return render(request, 'error/error-500.html')

    
