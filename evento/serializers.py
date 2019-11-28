from rest_framework import serializers
from .models import Evento, Categoria

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'
        default_permissions = ("view")

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        default_permissions = ("view",)

