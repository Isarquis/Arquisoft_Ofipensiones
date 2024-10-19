from django.db import models
from facturas.models import Factura

class Recibo(models.Model):
    id=models.AutoField(primary_key=True)
    fecha=models.DateTimeField(auto_now_add=True)
    direccion=models.CharField(max_length=30)
    ciudad= models.CharField(max_length=20)
    factura= models.ForeignKey(Factura, on_delete=models.CASCADE, default=None)
    def __str__(self) -> str:
        return '%s %s %s' % (self.id, self.factura.id, self.factura.estudiante.nombre)

    