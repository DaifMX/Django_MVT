from django.db import models

# Create your models here.
class familiares(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField()