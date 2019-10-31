from django.db import models
from doadores.models import Doadores
from datetime import datetime, date
    
class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60, blank=False)
    # id_doador = models.ForeignKey("Doador", on_delete=models.CASCADE, related_name = 'evento')
    data_inicio = models.DateTimeField(default=datetime.now)
    data_final = models.DateTimeField(default=datetime.now)
    # local = models.CharField(max_length=50, blank=False)
    desc = models.TextField(max_length=300, blank=False)
    doador  = models.ForeignKey(Doadores,on_delete=models.CASCADE)
    