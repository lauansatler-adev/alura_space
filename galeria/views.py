"""Responsável por cuidar do que vai ser exibido em cada página
    O que vai ser renderizado e o conteúdo que as páginas irão ter
"""


from django.shortcuts import render # Tem a função de renderizar páginas html
# Combina um ficheiro HTML com um dicionário de dados e devolve uma resposta HTTP completa para o navegador do ultilizador
from django.http import HttpResponse #Forma de conseguir responder uma requisição(enviar uma resposta HTTP)

# Função responsável pela página PRINCIPAL da aplicação
def index(request):  # para responder, preciso receber a requisição
    
    return render(request, 'galeria/index.html') #Primeiro parâmetro e passar devolta a requisição
    
    #return HttpResponse() # retorna a resposta em html
    
# Responsável por exibir imagem.html
def imagem(request):
    
    return render(request, 'galeria/imagem.html')
