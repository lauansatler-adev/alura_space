""" Responsável pelas ROTAS da app galeria"""

from django.urls import path # Usado para mapear endereços web (URLs) parafuncções de visualização (views)
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name='index'), # Rota da página principal
    path('imagem/', imagem, name='imagem') # Rota da página imagem.html
]