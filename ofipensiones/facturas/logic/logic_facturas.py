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

def get_facturas(cod_estudiante):
    try:
        facturas= Factura.objects.filter(estudiante__id=cod_estudiante)
        return facturas
    
    except:
        return "Estudiante no tiene factura"
