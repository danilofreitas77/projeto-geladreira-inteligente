from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from estoque.models import item
from .models import Compra

@csrf_exempt
def adicionar_carrinho(request):
    if request.method == 'POST':
        dados = json.loads(request.body)
        produto_id = dados.get('produto_id')
        quantidade = int(dados.get('quantidade'))

        try:
            produto = item.objects.get(id=produto_id)

            if quantidade > produto.quantidade:
                return JsonResponse({'status': 'erro', 'msg': 'Quantidade insuficiente no estoque'})

            # adiciona uma nova Compra para o usuário
            Compra.objects.create(
                usuario=request.user,
                item=produto,
                quantidade=quantidade
            )

            # dá baixa no estoque
            produto.quantidade -= quantidade
            produto.save()

            return JsonResponse({'status': 'ok'})

        except item.DoesNotExist:
            return JsonResponse({'status': 'erro', 'msg': 'Produto não encontrado'})

    return JsonResponse({'status': 'erro', 'msg': 'Método inválido'})

def ver_carrinho(request):
    # Pega todas as compras do usuário logado que ainda não foram finalizadas
    compras = Compra.objects.filter(usuario=request.user)

    # Calcula o total do carrinho
    total = sum([c.total() for c in compras])

    return render(request, 'compras/carrinho.html', {'compras': compras, 'total': total})