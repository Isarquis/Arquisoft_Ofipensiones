from django.db import models

class Colegio(models.Model):
    nombre=models.CharField(max_length=40)
    cuenta=models.IntegerField()
    direccion=models.CharField(max_length=30)
    codigo=models.AutoField(primary_key=True)
    correo=models.EmailField(max_length=60,null=True,blank=True)
    def __str__(self) -> str:
        return super().__str__()
