from django.urls import path
from . import views

urlpatterns = [
    path('api/carrinho/adicionar/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
]
