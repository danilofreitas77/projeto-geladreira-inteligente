from rest_framework import serializers
from .models import Compra

class CompraSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    total = serializers.ReadOnlyField()

    class Meta:
        model = Compra
        fielss = ['id', 'usuario', 'produto', 'quantidade', 'data', 'total']
=======
    class Meta:
        model = Compra
        fields = ['id', 'usuario', 'item', 'quantidade', 'data']
        read_only_fields = ['id', 'usuario', 'data']  # usuario vem do request
>>>>>>> atualizar-versao
