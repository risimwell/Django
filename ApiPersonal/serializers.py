from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from.models import Registro

class RegistroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = ('id','nombre','apellidos','cedula','clave','telefono','fechaDeNacimiento','correo','fotoPerfil','comoNosContacto','numeroDeHijos')
 

