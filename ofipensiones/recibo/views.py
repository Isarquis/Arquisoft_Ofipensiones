from django.shortcuts import render, get_object_or_404
from .models import Recibo

def base(request):
    return render(request, 'base.html')

def get_recibo(request, var_pk):
    recibo = get_object_or_404(Recibo, pk=var_pk)
    facturas = recibo.factura_set.all() 
    return render(request, 'recibo_detail.html', {'recibo': recibo, 'facturas': facturas})