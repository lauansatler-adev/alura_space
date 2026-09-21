""" Responsável pelas ROTAS da app galeria"""

from django.urls import path # Usado para mapear endereços web (URLs) para funcções de visualização (views)
from galeria.views import index, imagem, buscar

urlpatterns = [
    path('', index, name='index'), # Rota da página principal
    path('imagem/<int:foto_id>', imagem, name='imagem'), # Rota da página imagem.html
    path("buscar", buscar, name="buscar"),
]