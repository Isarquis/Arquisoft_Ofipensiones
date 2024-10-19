from .models import Recibo

def get_recibo(var_pk):
    recibo = Recibo.objects.get(pk=var_pk)
    facturas = recibo.facturas.all()  
    return recibo, facturas
