"""
    ##
    Importa o módulo de modelos de django para criar tabelas e gerir a base de dados usando código python
    Permite definir tabelas colunas e relações de base de dados como se fossem classes e atributos em python
    Cada classe que herda de models.Model transforma-se numa tabela na base de dados
    Disponibiliza tipos de dados como charField, IntegerField e DateField para definir as colunas de cada tabela
    ##
"""
from django.db import models ##

# Representa uma tabela no banco de dados
# Classe -> Model -> Tabela
class Fotografia(models.Model): # Herdando a biblioteca
    nome = models.CharField(max_length=100, null=False, blank=False) # Maximo de caracteries / Não pode ser vazio / Não pode ser uma string vazia
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    
    # Devolve o nome de cada item
    def __str__(self):
        return f"Fotografia [nome={self.nome}]"