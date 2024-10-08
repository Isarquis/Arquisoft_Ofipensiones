from django.db import models
from estudiante.models import Estudiante

class Factura(models.Model):
    id=models.AutoField(primary_key=True)
    estudiante=models.ForeignKey(Estudiante, on_delete=models.CASCADE,default=None)
    saldo=models.FloatField()
    fecha=models.DateTimeField(auto_now_add=True)
    cuenta_origen=models.CharField(max_length=15)
    cuenta_destino=models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return '%s %s %s' % (self.id, self.estudiante.nombre, self.fecha)
   