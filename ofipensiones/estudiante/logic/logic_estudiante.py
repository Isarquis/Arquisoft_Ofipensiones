from ..models import Estudiante



def get_colegioEstudiante(var_pk):
    try:
        estudiante=Estudiante.objects.get(codigo=var_pk)
        return estudiante.colegio
    except:
        return None
    

def get_estudiantes(var_pk):
    try:
        estudiante=Estudiante.objects.get(pk=var_pk)
        return estudiante
    except:
        return None

