from django.db import models
from django.contrib.auth.models import User
from estoque.models import item

class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(item, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def total(self):
<<<<<<< HEAD
        return self.produto.valor * self.quantidade  # "valor" conforme teu modelo item
=======
        return self.item.valor * self.quantidade

>>>>>>> atualizar-versao
