from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length = 100)
    quantidade = models.IntegerField()
    preço = models.FloatField()