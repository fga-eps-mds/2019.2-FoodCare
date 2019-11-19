from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Usuario
from .serializers import UsuarioSerializer, UserSerializer


class UsuarioSerializerViewSet(viewsets.ModelViewSet):

    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

class UserSerializerViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()