from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Doadores
from .serializers import DoadoresSerializer


class DoadoresViewSet(viewsets.ModelViewSet):
    serializer_class = DoadoresSerializer
    queryset = Doadores.objects.all()
