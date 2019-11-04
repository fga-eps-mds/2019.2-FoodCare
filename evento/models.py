from django.db import models
from datetime import datetime, date
from users.models import Usuario

class Evento(models.Model):
    
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60, blank=False)
    id_doador = models.ForeignKey('users.Usuario', on_delete=models.CASCADE)
    data_inicio = models.DateTimeField(default=datetime.now)
    data_final = models.DateTimeField(default=datetime.now)
    local = models.CharField(max_length=50, blank=False)
    desc = models.TextField(max_length=300, blank=False)
