from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.categorias, name='categorias'),
    path('categoria/<str:categoria>/', views.listar_por_categoria, name='listar_por_categoria'),
    path('categorias/', views.categorias, name='categorias'),

]
