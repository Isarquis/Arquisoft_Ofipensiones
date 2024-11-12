from ..models import Factura

def get_factura(var_pk):
    try:
        factura=Factura.objects.get(pk=var_pk)
        return factura
    except:
        return None

def delete_factura(var_pk):
    try:
         factura=Factura.objects.get(pk=var_pk)
         factura.delete()
         return "Factura eliminada"
    except:
        return "Factura no existe"
