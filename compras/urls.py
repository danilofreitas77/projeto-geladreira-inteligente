from rest_framework.routers import DefaultRouter
from .views import CompraViewSet
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'compras', CompraViewSet)

urlpatterns = [
    path('carrinho/', views.carrinho, name='carrinho'),
]