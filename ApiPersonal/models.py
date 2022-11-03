
from django.db import models


# Create your models here.
class Registro(models.Model):
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    cedula = models.TextField()
    clave = models.TextField()
    telefono = models.IntegerField()
    fechaDeNacimiento= models.DateField()
    correo = models.EmailField()
    fotoPerfil = models.ImageField(upload_to= "ApiPersonal\Imagenes",null=True,blank=True)
    comoNosContacto = models.TextField()
    numeroDeHijos = models.IntegerField()






