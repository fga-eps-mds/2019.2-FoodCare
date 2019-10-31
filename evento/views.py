from rest_framework import viewsets
from .models import Evento
from doadores.models import Doadores
from doadores.serializers import DoadoresSerializer
from .serializers import EventoSerializer


class EventoViewSet(viewsets.ModelViewSet):

    serializer_class = EventoSerializer
    queryset = Evento.objects.all()

class DoadoresViewSet(viewsets.ModelViewSet):
    serializer_class  = DoadoresSerializer
    queryset = Doadores.objects.all()