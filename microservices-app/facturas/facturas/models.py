from django.db import models

class Factura(models.Model):
    id=models.AutoField(primary_key=True)
    estudiante=models.IntegerField(null=False, default=None)
    saldo=models.FloatField()
    fecha=models.DateTimeField(auto_now_add=True)
    cuenta_origen=models.CharField(max_length=15)
    cuenta_destino=models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return '%s %s %s' % (self.id, self.estudiante.codigo, self.fecha)