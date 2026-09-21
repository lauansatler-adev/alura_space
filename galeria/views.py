"""Responsável por cuidar do que vai ser exibido em cada página
    O que vai ser renderizado e o conteúdo que as páginas irão ter
"""

from django.shortcuts import render, get_object_or_404 # Tem a função de renderizar páginas html
# Combina um ficheiro HTML com um dicionário de dados e devolve uma resposta HTTP completa para o navegador do ultilizador
from django.http import HttpResponse #Forma de conseguir responder uma requisição(enviar uma resposta HTTP)
from galeria.models import Fotografia

# Função responsável pela página PRINCIPAL da aplicação
def index(request):  # para responder, preciso receber a requisição
    # Puxa os itens do banco de dados em forma de objeto
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicado=True) # Vai pegar todos os itens do banco de dados onde o campo publicado seja verdadeiro
    #Ordenado por datar
    
    
    # O render também permite enviar informações dentro de um dicionário
    return render(request, 'galeria/index.html', {"cards": fotografias}) #Primeiro parâmetro e passar devolta a requisição
    
    #return HttpResponse() # retorna a resposta em html
    
# Responsável por exibir imagem.html
def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id) #Ou pega o objeto ou tras um não encontrado
    
    # O render também permite enviar informações dentro de um dicionário
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    
    return render(request, "galeria/buscar.html")
