from django.shortcuts import render
from .models import Factura
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json
from .logic import logic as lf
from ofipensiones.auth0backend import getRole


def check_usuario(data):
    r = requests.get(settings.PATH_USER, headers={"Accept":"application/json"})
    usuarios = r.json()
    for usuario in usuarios:
        if data["estudiante"] == usuarios["id"]:
            return usuario
    return False

def check_colegio(data):
    r = requests.get(settings.PATH_COLEGIOS, headers={"Accept":"application/json"})
    places = r.json()
    for place in places:
        if data["place"] == place["name"]:
            return place["id"]
    return -1

def check_colegio_mail(data):
    r = requests.get(settings.PATH_COLEGIOS, headers={"Accept":"application/json"})
    colegios = r.json()
    for colegio in colegios:
        if data["place"] == place["name"]:
            return place["id"]
    return -1

def facturas_view(request, id):
    role= getRole(request)
    if role=="Gerente":
        codigoEstudiante = lf.get_factura(id).estudiante
        print(codigoEstudiante)
        colegioGerente = lc.get_colegio(request.user.email)
        colegioEstudiante = le.get_colegioEstudiante(codigoEstudiante.codigo)
        if colegioGerente.codigo == colegioEstudiante.codigo:
            if request.method == 'GET':
                lf.delete_factura(id)
                return HttpResponse("borro su bendita factura")
        else:
            return HttpResponse("Gerente de otro colegio")
        
    else:
        return HttpResponse("Unauthorized User")

def facturas_estudiante_view(request, cod):
    role=getRole(request)
    if role=="Estudiante":
        if request.method=='GET':
            
            facturas=lf.get_facturas(cod)
            if facturas[0].estudiante.correo==request.user.email:
                return HttpResponse(facturas, 'application/json')
            else:
                return HttpResponse("No tiene acceso")
    else:
        return HttpResponse("No tiene acceso")
