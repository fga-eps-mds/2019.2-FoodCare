from django.db import models
from datetime import datetime, date
from users.models import Usuario

class Evento(models.Model):

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60, blank=False)
    desc = models.TextField(max_length=300, blank=False)
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=False)
    data_inicio = models.DateTimeField(default=datetime.now)
    data_final = models.DateTimeField(default=datetime.now)
    id_doador = models.ForeignKey('users.Usuario', on_delete=models.CASCADE)
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.nome, self.id_doador.id)

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60, blank=False) 

    def __str__(self):
        return "{}".format(self.nome)

