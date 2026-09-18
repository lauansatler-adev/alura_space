""" Responsável pelas ROTAS da aplicação"""

from django.contrib import admin #importa o modulo de adiministração do Django
from django.urls import path, include # Usado para mapear endereços web (URLs) parafuncções de visualização (views)


"""Include trás todas as rotas da app passada com um ponto (.) 
    para determinar o arquivo onde os caminhos estão armazenados
    sendo normalmento um arquivo com o nome de urls.py onde cada app pode ter o seu
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')), #Include
    
]
