from .models import Facturas
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json

def check_variable(data):
    r = requests.get(settings.PATH_VAR, headers={"Accept":"application/json"})
    variables = r.json()
    for variable in variables:
        if data["variable"] == variable["id"]:
            return True
    return False

def get_institucion_id(data):
    r = requests.get(settings.PATH_INSTITUCION, headers={"Accept":"application/json"})
    institucion = r.json()
    for inst in institucion:
        if data["institucion"] == inst["name"]:
            return inst["id"]
    return -1

def FacturasList(request):
    queryset = Facturas.objects.all()
    context = list(queryset.values('id', 'variable', 'value', 'unit', 'place', 'dateTime'))
    return JsonResponse(context, safe=False)

def FacturasCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_variable(data_json):
            Facturas = Facturas()
            Facturas.variable = data_json['variable']
            Facturas.value = data_json['value']
            Facturas.unit = data_json['unit']
            Facturas.place = data_json['place']
            Facturas.save()
            return HttpResponse("successfully created Facturas")
        else:
            return HttpResponse("unsuccessfully created Facturas. Variable or place does not exist")

def FacturassCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        Facturas_list = []
        for Facturas in data_json:
                    if check_variable(Facturas) == True:
                        db_Facturas = Facturas()
                        db_Facturas.variable = Facturas['variable']
                        db_Facturas.value = Facturas['value']
                        db_Facturas.unit = Facturas['unit']
                        db_Facturas.place = Facturas['place']
                        Facturas_list.append(db_Facturas)
                    else:
                        return HttpResponse("unsuccessfully created Facturas. Variable or place does not exist")
        
        Facturas.objects.bulk_create(Facturas_list)
        return HttpResponse("successfully created Facturass")