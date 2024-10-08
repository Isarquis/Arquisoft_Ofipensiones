from django.shortcuts import render
from .logic import logic_facturas as lf
from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Factura

@csrf_exempt
def factura_view(request, id):
    if request.method== 'GET':
        factura_dto=lf.get_factura(id)
        factura=serializers.serialize('json', [factura_dto])
        return HttpResponse(factura, 'application/json')
        
            
def mostrar_factura(request, id):
    factura = get_object_or_404(Factura, id=factura_id)
    return render(request, 'factura_detalle.html', {'factura': factura})