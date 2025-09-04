from rest_framework import serializers
from .models import Compra

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = ['id', 'usuario', 'item', 'quantidade', 'data']
        read_only_fields = ['id', 'usuario', 'data']  # usuario vem do request
