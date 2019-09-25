from django.db import models
from datetime import datetime, date

class Evento(models.Model):
    endereco = models.CharField(max_length=60, blank=False)
    data_inicio = models.DateField(blank=True)
    hora_inicio = models.TimeField(blank=False)
    data_fim = models.DateField(blank=True)
    hora_fim = models.TimeField(blank=False)

