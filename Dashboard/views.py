from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Electricity.models import Medida, Inversor
import  Electricity.calculos as calculos
from django.db.models.functions import TruncHour
from django.utils import timezone


@login_required
def home(request):
    
    context = {}
    context['energia_dia_total'] = calculos.energia('dia')
    context['energia_semana'] = calculos.energia('semana',1)
    context['energia_mes'] = calculos.energia('mes',1)

    return render(request, 'dashboard/index.html',context)

def handler400(request, exception):
    return render(request, 'error/error-404.html')

def handler403(request, exception):
    return render(request, 'error/error-404.html')

def handler404(request, exception):
    return render(request, 'error/error-404.html')

def handler500(request):
    return render(request, 'error/error-500.html')


