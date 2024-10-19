from ..models import Recibo

def get_recibo(var_pk):
    factura=Recibo.objects.get(pk=var_pk)
    return factura
