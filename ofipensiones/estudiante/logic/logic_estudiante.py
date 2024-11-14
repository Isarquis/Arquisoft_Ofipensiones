from ..models import Estudiante

def get_colegioEstudiante(var_pk):
    try:
        estudiante=Estudiante.objects.get(codigo=var_pk)
        return estudiante.colegio
    except:
        return None