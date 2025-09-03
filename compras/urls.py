from django.urls import path
from . import views

urlpatterns = [
    path('carrinho/', views.ver_carrinho, name='carrinho'),
]
