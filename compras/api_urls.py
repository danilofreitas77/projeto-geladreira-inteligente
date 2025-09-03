from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompraViewSet, adicionar_carrinho

router = DefaultRouter()
router.register(r'compras', CompraViewSet, basename='compras')

urlpatterns = [
    path('', include(router.urls)),
    path('carrinho/', adicionar_carrinho, name='api_adicionar_carrinho'),
]
