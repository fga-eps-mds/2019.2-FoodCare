from rest_framework import viewsets
from .models import Evento, Alimento
from .serializers import EventoSerializer, AlimentoSerializer


class EventoViewSet(viewsets.ModelViewSet):

    serializer_class = EventoSerializer
    queryset = Evento.objects.all()


class AlimentoViewSet(viewsets.ModelViewSet):

    serializer_class = AlimentoSerializer
    queryset = Alimento.objects.all()
