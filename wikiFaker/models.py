from django.db import models

# Create your models here.
class t1(models.Model):
    nombre           = models.CharField(primary_key=True,max_length=30)
    posicion         = models.CharField(max_length=50)
    nickname         = models.CharField(max_length=30)
    nacionalidad     = models.CharField(max_length=30)
    foto             = models.CharField(max_length=9999)
    def __str__(self):
        return str(self.nombre)
