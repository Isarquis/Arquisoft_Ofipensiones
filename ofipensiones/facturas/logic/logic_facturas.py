from ..models import Factura

def get_factura(var_pk):
    factura=Factura.objects.get(pk=var_pk)
    return factura