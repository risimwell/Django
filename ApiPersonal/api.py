from.models import Registro
from rest_framework import viewsets, permissions
from .serializers import RegistroSerializers


class RegistroviewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegistroSerializers