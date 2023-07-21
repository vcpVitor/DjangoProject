from django.db import models

class Pelucia(models.Model):
    modelo = models.CharField(max_length=50)
    cor = models.CharField(max_length=50)
    coracao = models.BooleanField()
    tamanho = models.CharField(max_length=2)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.modelo} {self.cor} {self.tamanho}"