from rest_framework import viewsets
from .models import Evento
from .serializers import EventoSerializer


class EventoViewSet(viewsets.ModelViewSet):

    serializer_class = EventoSerializer
    queryset = Evento.objects.all()