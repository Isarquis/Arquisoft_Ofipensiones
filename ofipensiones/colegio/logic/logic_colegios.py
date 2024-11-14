from ..models import Colegio


def get_colegio(var_pk):
    try:
        colegio=Colegio.objects.get(correo=var_pk)
        return colegio
    except:
        return None
def get_correo(var_pk):
    try:
        colegio=Colegio.objects.get(pk=var_pk)
        return colegio.correo
    except:
        return None
def get_colegios():
    try:
        colegios=Colegio.objects.all()
        return colegios
    except:
        return None



