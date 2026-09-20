"""
    ##
    Importa o módulo de modelos de django para criar tabelas e gerir a base de dados usando código python
    Permite definir tabelas colunas e relações de base de dados como se fossem classes e atributos em python
    Cada classe que herda de models.Model transforma-se numa tabela na base de dados
    Disponibiliza tipos de dados como charField, IntegerField e DateField para definir as colunas de cada tabela
    ##
"""
from django.db import models ##
from datetime import datetime

""" ========Toda vez que alter o model é preciso fazer migratrion========="""

# Representa uma tabela no banco de dados
# Classe -> Model -> Tabela
class Fotografia(models.Model): # Herdando a biblioteca
    
    # E preciso ser uma tupla pois o método CharField foi criado para interpretar tuplas
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta")
    ]
    
    nome = models.CharField(max_length=100, null=False, blank=False) # Maximo de caracteries / Não pode ser vazio / Não pode ser uma string vazia
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default="")
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)# Cria um campo onde posso selecionar um arquivo de imagem
    publicado = models.BooleanField(default=False) # Cria un campo com uma checkbox
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False) #Cria um campo com a data de hora da modificação
    
    # Devolve o nome de cada item
    def __str__(self):
        return self.nome