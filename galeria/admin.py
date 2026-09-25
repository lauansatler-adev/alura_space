""" ##### Aqui se faz todas as mudanças que diz respeito ao django admin #####"""

""" Disponibiliza as ferramentas de adiministração do django no seu arquivo (geralmente admin.py
    
    Com o objeto admin, voce pode usar admin.site.register(MeuModelo) para exibir e gerenciar
    suas tabelas e dados diretamente do navegador
"""
from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicado", ) # Formata a forma como a tabela é apresentada
    list_display_links = ("id", "nome", )# Muda o que é um link na tabela
    search_fields = ("nome", ) # Adiciona um campo de busca no django admin
    list_filter = ("categoria", "usuario") # Adiciona um filtro pela categoria
    list_editable = ("publicado", )
    list_per_page = 10 # Responsável por dizer quantos itens da tabela vão ser mostrado por vez

admin.site.register(Fotografia, ListandoFotografias) # Registrando o banco de dados com o django admin