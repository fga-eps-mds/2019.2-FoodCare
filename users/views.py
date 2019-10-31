from django.shortcuts import render
from rest_framework import viewsets

from .models import Usuario
from .serializers import UsuarioSerializer


class UsuarioSerializerViewSet(viewsets.ModelViewSet):

    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()