# compras/views.py
from django.http import JsonResponse
from .models import Compra
from estoque.models import item
from django.contrib.auth.decorators import login_required
import json
from django.shortcuts import render

@login_required
def adicionar_carrinho(request):
    if request.method == "POST":
        dados = json.loads(request.body)
        produto_id = dados.get('produto_id')
        quantidade = int(dados.get('quantidade', 1))

        try:
            produto = item.objects.get(id=produto_id)

            # get_or_create com defaults para evitar NOT NULL error
            # Verifica se já existe no carrinho
            compra, criado = Compra.objects.get_or_create(
                usuario=request.user,
                item=produto,
                defaults={'quantidade': quantidade}
            )

            if not criado:
                compra.quantidade += quantidade
            else:
                compra.quantidade = quantidade

            compra.save()

            # Subtrair do estoque **apenas a quantidade adicionada agora**
            produto.quantidade -= quantidade
            produto.save()


            return JsonResponse({
                "status": "ok",
                "produto": produto.produto,
                "quantidade": compra.quantidade
            })

        except item.DoesNotExist:
            return JsonResponse({"status": "erro", "msg": "Produto não encontrado"}, status=404)

    return JsonResponse({"status": "erro", "msg": "Método inválido"}, status=400)

@login_required
def ver_carrinho(request):
    # pega todas as compras do usuário
    compras = Compra.objects.filter(usuario=request.user)

    # calcula o total do carrinho
    total = sum([c.total() for c in compras])

    context = {
        'compras': compras,
        'total': total
    }
    return render(request, 'compras/carrinho.html', context)


@login_required
def remover_carrinho(request):
    if request.method == "POST":
        dados = json.loads(request.body)
        produto_id = dados.get('produto_id')

        try:
            compra = Compra.objects.get(usuario=request.user, item_id=produto_id)
            produto = compra.item

            # Devolve ao estoque
            produto.quantidade += compra.quantidade
            produto.save()

            # Remove do carrinho
            compra.delete()

            return JsonResponse({"status": "ok", "msg": "Item removido do carrinho"})
        except Compra.DoesNotExist:
            return JsonResponse({"status": "erro", "msg": "Item não encontrado no carrinho"}, status=404)

    return JsonResponse({"status": "erro", "msg": "Método inválido"}, status=400)
