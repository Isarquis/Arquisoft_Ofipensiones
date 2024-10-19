from django.db import models
from estudiante.models import Estudiante
from facturas.models import Facturas

class Recibo(models.Model):
    id=models.AutoField(primary_key=True)
    estudiante=models.ForeignKey(Estudiante, on_delete=models.CASCADE,default=None)
    fecha=models.DateTimeField(auto_now_add=True)
    valor=models.FloatField()
    facturas=models.ForeignKey(Facturas, on_delete=models.CASCADE,default=None)

    

    
    def __str__(self) -> str:
        return '%s %s %s %s' % (self.id, self.estudiante.nombre, self.fecha, self.valor)
    class Meta:
        db_table = 'Recibo'