from django.db import models
from datetime import datetime, date

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    

class Alimento(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    un_medida = models.CharField(max_length=60)
    quantidade = models.IntegerField()
    id_categoria = models.ManyToManyField(Categoria)
    

class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    #id_doador = models.ForeignKey("Doador", on_delete=models.CASCADE, related_name = 'evento')
    #id_endereco = models.ForeignKey("Endereco", on_delete=models.CASCADE, related_name = 'evento')
    id_alimento = models.ManyToManyField(Alimento)
    data_inicio = models.DateTimeField(default=datetime.now)
    data_final = models.DateTimeField(default=datetime.now)
    

