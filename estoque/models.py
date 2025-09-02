from django.db import models

class item(models.Model):
    produto = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    
    CATEGORIAS = [
        ('bebida', 'Bebida'),
        ('comida', 'Comida'),
    ]
    categoria = models.CharField(max_length=10, choices=CATEGORIAS)

    def __str__(self):
        return self.produto
