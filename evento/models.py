from django.db import models
from datetime import datetime, date

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    

class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    #id_doador = models.ForeignKey("Doador", on_delete=models.CASCADE, related_name = 'evento')
    #id_endereco = models.ForeignKey("Endereco", on_delete=models.CASCADE, related_name = 'evento')
    data_inicio = models.DateTimeField(default=datetime.now)
    data_final = models.DateTimeField(default=datetime.now)
    local = models.CharField(max_length=50, blank=False)

class Alimento(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    un_medida = models.CharField(max_length=60)
    quantidade = models.IntegerField()
    id_categoria = models.ManyToManyField(Categoria)
    id_evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    