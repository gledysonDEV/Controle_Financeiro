from django.contrib.auth.models import User
from django.db import models

class Transacao(models.Model):
    TIPO_CHOICES = [
        ('Receita', 'Receita'),
        ('Despesa', 'Despesa'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    categoria = models.CharField(max_length=100)
    data = models.DateField()

    def __str__(self):
        return f"{self.descricao} | {self.tipo} | {self.valor}"