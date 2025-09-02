from django.shortcuts import render
from .models import item  # ou Produto, como você chamou

def listar_produtos(request, categoria=None):
    if categoria:
        produtos = item.objects.filter(categoria=categoria)
    else:
        produtos = item.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})

