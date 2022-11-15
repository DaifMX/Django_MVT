from django.db import models
# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField()


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    sku = models.CharField(max_length=20)
    stock = models.IntegerField()


class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    rfc = models.CharField(max_length=13)
    direccion = models.CharField(max_length=50)



