from django.db import models
from estudiante.models import Estudiante
class Facturacion(models.Model):
    estudiante=models.ForeignKey(Estudiante, on_delete=models.CASCADE,default=None)
    saldo=models.FloatField()
    fecha=models.DateTimeField(auto_now_add=True)
    cuenta_origen=models.CharField(max_length=15)
    cuenta_destino=models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return '%s' % (self.estudiante.nombre, self.saldo, self.fecha, self.cuenta_origen, self.cuenta_destino)
# Create your models here.