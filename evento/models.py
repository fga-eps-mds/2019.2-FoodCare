from django.db import models
from datetime import datetime, date

class Alimento(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    un_medida = models.CharField(max_length=60)
    quantidade = models.IntegerField()

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    #id_alimento = models.ForeignKey("Alimento", on_delete=models.CASCADE, related_name='categoria')

class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    #id_doador = models.ForeignKey("Doador", on_delete=models.CASCADE, related_name = 'evento')
    #id_endereco = models.ForeignKey("Endereco", on_delete=models.CASCADE, related_name = 'evento')
    #id_alimento = models.ManyToManyField(Alimento)
    # esta dando erro aqui, nao consegui resolver, mas o campo deve ser DateTime de acordo com o DER
    #hora_inicio = models.DateTimeField(default=datetime.now)
    #hora_final = models.DateTimeField(default=datetime.now)
    data_inicio = models.DateField(blank=True)
    hora_inicio = models.TimeField(blank=False)
    data_fim = models.DateField(blank=True)
    hora_fim = models.TimeField(blank=False)

