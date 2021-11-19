from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length = 20)
    cr = models.IntegerField()

    def __str__(self) -> str:
        return f'Nome: {self.nome} <br> CR: {self.cr}'