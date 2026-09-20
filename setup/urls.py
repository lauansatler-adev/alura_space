""" Responsável pelas ROTAS da aplicação"""

from django.contrib import admin #importa o modulo de adiministração do Django
from django.urls import path, include # Usado para mapear endereços web (URLs) para funções de visualização (views)
from django.conf import settings
from django.conf.urls.static import static

""" ## Include trás todas as rotas da app passada com um ponto (.) 
    para determinar o arquivo onde os caminhos estão armazenados
    sendo normalmento um arquivo com o nome de urls.py onde cada app pode ter o seu
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')), #Include ##
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Indica que precisa ultilizar as referências que foi adicionado no settings.py



