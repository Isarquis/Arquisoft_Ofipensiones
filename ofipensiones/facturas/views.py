from django.shortcuts import render
from .logic import logic_facturas as lf
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ofipensiones.auth0backend import getRole
from ofipensiones.auth0backend import Auth0

@csrf_exempt
def factura_view(request, id):
    if request.method== 'GET':
        factura_dto=lf.get_factura(id)
        if factura_dto:
            factura=serializers.serialize('json', [factura_dto])
            return HttpResponse(factura, 'application/json')
        else:
            return HttpResponse("Factura no encontrada")

    
def facturas_view(request, id):
    role= getRole(request)
    if role=="Gerente":
        email=request.user['email']
        if request.method == 'GET':
            factura_dto=lf.delete_factura(id)
            return HttpResponse(factura_dto)
    else:
        return HttpResponse("Unauthorized User")
    
def facturas_estudiante_view(request, cod):
    if request.method=='GET':
        facturas_dto=lf.get_facturas(cod)
        return HttpResponse(facturas_dto, 'application/json')