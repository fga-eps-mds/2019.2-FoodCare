from django.db import models

# Create your models here.
class Doadores(models.Model):
    nome = models.CharField(max_length=60)
    cpnj = models.CharField(max_length=14)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=50)