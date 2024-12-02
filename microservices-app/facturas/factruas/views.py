from .models import Facturas
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json

def check_usuarios(data):
    r = requests.get(settings.PATH_VAR, headers={"Accept":"application/json"})
    usuarioss = r.json()
    for usuarios in usuarioss:
        if data["usuarios"] == usuarios["id"]:
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
    context = list(queryset.values('id', 'usuarios', 'value', 'unit', 'institucion', 'dateTime'))
    return JsonResponse(context, safe=False)

def FacturasCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_usuarios(data_json):
            Facturas = Facturas()
            Facturas.usuarios = data_json['usuarios']
            Facturas.value = data_json['value']
            Facturas.unit = data_json['unit']
            Facturas.institucion = data_json['institucion']
            Facturas.save()
            return HttpResponse("successfully created Facturas")
        else:
            return HttpResponse("unsuccessfully created Facturas. usuarios or institucion does not exist")

def FacturassCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        Facturas_list = []
        for Facturas in data_json:
                    if check_usuarios(Facturas) == True:
                        db_Facturas = Facturas()
                        db_Facturas.usuarios = Facturas['usuarios']
                        db_Facturas.value = Facturas['value']
                        db_Facturas.unit = Facturas['unit']
                        db_Facturas.institucion = Facturas['institucion']
                        Facturas_list.append(db_Facturas)
                    else:
                        return HttpResponse("unsuccessfully created Facturas. usuarios or institucion does not exist")
        
        Facturas.objects.bulk_create(Facturas_list)
        return HttpResponse("successfully created Facturass")