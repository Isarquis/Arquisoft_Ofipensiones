from django.db import models
from colegio.models import Colegio
class Estudiante(models.Model):
    nombre=models.CharField(max_length=60)    
    grado=models.IntegerField()
    colegio=models.ForeignKey(Colegio, on_delete=models.CASCADE, default=None)
    
    def __str__(self) -> str:
        return '%s' % (self.nombre)
