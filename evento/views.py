from rest_framework import viewsets
from .models import Evento, Categoria
from .serializers import EventoSerializer, CategoriaSerializer


class EventoViewSet(viewsets.ModelViewSet):

    serializer_class = EventoSerializer
    queryset = Evento.objects.all()

class CategoriaViewSet(viewsets.ModelViewSet):

    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()
