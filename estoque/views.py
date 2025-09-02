from django.shortcuts import render
from .models import item

def categorias(request):
    # Tela com botões: Bebidas e Comidas
    return render(request, 'estoque/categorias.html')

def listar_por_categoria(request, categoria):
    produtos = item.objects.filter(categoria=categoria)
    return render(request, 'estoque/listar_produtos.html', {'produtos': produtos, 'categoria': categoria})

def listar_produtos(request, categoria=None):
    if categoria:
        produtos = item.objects.filter(categoria=categoria)
    else:
        produtos = item.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})