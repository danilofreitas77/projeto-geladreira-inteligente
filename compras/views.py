from django.shortcuts import render
from rest_framework import viewsets
from .models import Compra
from .serializers import CompraSerializer

class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer


def carrinho(request):
    return render(request, 'compras/carrinho.html')
