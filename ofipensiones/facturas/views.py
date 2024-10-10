from django.shortcuts import render
from .logic import logic_facturas as lf
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def factura_view(request, id):
    if request.method== 'GET':
        factura_dto=lf.get_factura(id)
        factura=serializers.serialize('json', [factura_dto])
        return render(request, 'facturas/factura_detail.html', {'factura_id': id})