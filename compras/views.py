from django.shortcuts import render
from rest_framework import viewsets
from .models import Compra
from .serializers import CompraSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required


class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer


def carrinho(request):
    return render(request, 'compras/carrinho.html')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def adicionar_carrinho(request):
    user = request.user
    item_id = request.data.get('item')
    quantidade = int(request.data.get('quantidade', 0))

    item = item.objects.get(id=item_id)

    if quantidade <= 0 or quantidade > item.quantidade:
        return Response({'erro': 'Quantidade inválida'}, status=400)

    # cria compra (carrinho)
    Compra.objects.create(usuario=user, item=item, quantidade=quantidade)

    # baixa no estoque
    item.quantidade -= quantidade
    item.save()

    return Response({'success': 'Produto adicionado ao carrinho'})

@login_required
def ver_carrinho(request):
    compras = Compra.objects.filter(usuario=request.user)
    total = sum(c.total() for c in compras)
    return render(request, 'compras/carrinho.html', {'compras': compras, 'total': total})
