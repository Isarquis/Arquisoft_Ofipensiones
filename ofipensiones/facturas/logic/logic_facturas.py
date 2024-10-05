from ..models import Factura

def get_factura(estudiante, fecha):
    factura=Factura.objects.get(pk=var_pk)
    return factura