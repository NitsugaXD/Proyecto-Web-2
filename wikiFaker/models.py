from django.db import models

# Create your models here.
class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return str(self.genero)
    
class usuario(models.Model):
    id_usuario = models.AutoField(db_column='idUsuario',primary_key=True) 
    usuario = models.CharField(max_length=50, unique=True)
    id_genero  = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero') 
    correo = models.EmailField(max_length=200, unique=True)
    contraseña = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return str(self.usuario)


class puntos(models.Model):
    id_punto = models.AutoField(db_column='idPunto',primary_key=True) 
    puntos = models.IntegerField(unique=True)
    fecha_hora = models.CharField(max_length=100, unique=True)
    id_usuario  = models.ForeignKey('usuario',on_delete=models.CASCADE, db_column='idUsuario')  
    def __str__(self):
        return str(self.puntos)
class t1(models.Model):
    nombre           = models.CharField(primary_key=True,max_length=30)
    posicion         = models.CharField(max_length=50)
    nickname         = models.CharField(max_length=30)
    nacionalidad     = models.CharField(max_length=30)
    foto             = models.CharField(max_length=9999)
    def __str__(self):
        return str(self.nombre)


