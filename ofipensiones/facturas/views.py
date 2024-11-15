from django.shortcuts import render
from .logic import logic_facturas as lf
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ofipensiones.auth0backend import getRole
from colegio.logic import logic_colegios as lc
from estudiante.logic import logic_estudiante as le
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
    if request.method=='GET':
        facturas_dto=lf.get_facturas(cod)
        return HttpResponse(facturas_dto, 'application/json')
    
