from rest_framework import serializers
from .models import Compra

class CompraSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()

    class Meta:
        model = Compra
        fielss = ['id', 'usuario', 'produto', 'quantidade', 'data', 'total']