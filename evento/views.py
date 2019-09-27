from rest_framework import viewsets
from .models import Evento, Alimento, Categoria
from .serializers import EventoSerializer, AlimentoSerializer, CategoriaSerializer


class EventoViewSet(viewsets.ModelViewSet):

    serializer_class = EventoSerializer
    queryset = Evento.objects.all()


class AlimentoViewSet(viewsets.ModelViewSet):

    serializer_class = AlimentoSerializer
    queryset = Alimento.objects.all()


class CategoriaViewSet(viewsets.ModelViewSet):

    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()
