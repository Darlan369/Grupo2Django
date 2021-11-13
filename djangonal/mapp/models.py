from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length = 20)
    cr = models.IntegerField()