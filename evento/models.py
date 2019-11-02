from django.db import models
from datetime import datetime, date
from users.models import Usuario

class Evento(models.Model):
    """
    # Cria um evento
    >>> evento = EventoEvento.objects.create(
            nome="Teste",
            id_doador= id_doador, 
            data_inicio=datetime.now(), 
            data_final=datetime.now(), 
            desc="Apenas um teste"
            )

    # Fala o nome
    >>> evento.getNome()
    'Teste'
    """
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60, blank=False)
    id_doador = models.ForeignKey('users.Usuario', on_delete=models.CASCADE)
    data_inicio = models.DateTimeField(default=datetime.now)
    data_final = models.DateTimeField(default=datetime.now)
    desc = models.TextField(max_length=300, blank=False)
    
    def getID(self):
        return self.id_doador