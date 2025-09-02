from django.db import models

class item(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    quantidade = models.IntegerField()
    categoria = models.CharField(max_length=100, default="Outros")
    
    def __str__(self):
        return f"{self.nome} ({self.quantidade} unid.)"