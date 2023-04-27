from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import Http404
from .models import Medida, Inversor

@csrf_exempt
def insert_data(request):
    if request.POST:
        context = {}
        try:
            print(request.POST)
            painel = Inversor.objects.get(number=request.POST['painel'])
            print(painel)
            Medida(
                painel=painel,
                energia_diaV2=request.POST['energia_diaV2'],
                energia_ano=request.POST['energia_ano'],
                energia_total=request.POST['energia_total'],
                potenciav2=request.POST['potenciav2'],
                power_led=request.POST['power_led'],
                solarnet_led=request.POST['solarnet_led'],
                solarweb_led=request.POST['solarweb_led'],
                ).save()
            context['status'] = True
        except Exception as error:
            print(error)
            context['status'] = False
        
        return JsonResponse(context)
    return redirect('home')    

