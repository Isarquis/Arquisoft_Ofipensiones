from django.shortcuts import render
from .logic import logic_recibo as lr
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from facturas.logic import logic_facturas as lf
@csrf_exempt
def recibo_view(request, id):
    if request.method== 'GET':
        recibo_dto=lr.get_recibo(id)
        factura_dto=lf.get_factura(recibo_dto.factura.pk)
        factura=serializers.serialize('json', [factura_dto])
        recibo=serializers.serialize('json', [recibo_dto])
        return HttpResponse(recibo+factura, 'application/json')