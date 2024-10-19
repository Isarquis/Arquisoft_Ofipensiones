from ..models import Recibo

def get_recibo(var_pk):
    recibo=Recibo.objects.get(pk=var_pk)
    return recibo

