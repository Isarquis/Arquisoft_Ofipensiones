from ..models import Factura

def get_factura(var_pk):
    try:
        factura=Factura.objects.get(pk=var_pk)
        return factura
    except:
        return None