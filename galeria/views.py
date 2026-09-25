"""Responsável por cuidar do que vai ser exibido em cada página
    O que vai ser renderizado e o conteúdo que as páginas irão ter
"""

from django.shortcuts import render, get_object_or_404, redirect # Tem a função de renderizar páginas html
# Combina um ficheiro HTML com um dicionário de dados e devolve uma resposta HTTP completa para o navegador do ultilizador
from django.http import HttpResponse #Forma de conseguir responder uma requisição(enviar uma resposta HTTP)
from galeria.models import Fotografia
from django.contrib import messages

# Função responsável pela página PRINCIPAL da aplicação
def index(request):  # para responder, preciso receber a requisição
    
    if not request.user.is_authenticated: # Verifica se o usuiário esta autenticado
        messages.error(request, "Usuário não logado")
        return redirect("login") # Caso não, retorna a página de login
    
    # Puxa os itens do banco de dados em forma de objeto
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicado=True) # Vai pegar todos os itens do banco de dados onde o campo publicado seja verdadeiro
    #Ordenado por datar
    
    
    # O render também permite enviar informações dentro de um dicionário
    return render(request, 'galeria/index.html', {"cards": fotografias}) #Primeiro parâmetro e passar devolta a requisição
    
    #return HttpResponse() # retorna a resposta em html
    
# Responsável por exibir imagem.html
def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id) #Ou pega o objeto com o id indicado ou tras um não encontrado
    #PK pega a primary key que vem com o foto_id, que é passado pelo arquivo index.html nesse trecho <a href="{% url 'imagem' fotografia.id %}">
    
    
    # O render também permite enviar informações dentro de um dicionário
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    
    
    if not request.user.is_authenticated: # Verifica se o usuiário esta autenticado
        messages.error(request, "Usuário não logado")
        return redirect("login") # Caso não, retorna a página de login
        
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicado=True)
    
    # Confere se existe o termo buscar dentro das informações passadas pela url/ Essa informação fica em request.GET
    if "buscar" in request.GET:    
        
        # Coloca na variável nome_a_bucar o que foi digitado na caixa de pesquisa
        nome_a_buscar = request.GET["buscar"] # O buscar faz referência ao que colocamos no arquivo "_menu.html", dentro do <input>: o name "buscar", localizado na linha de código 8.
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar) # Busca se existe alguima parte que faz sentido co o nome que está sendo buscado
    
    return render(request, "galeria/buscar.html", {"cards": fotografias})
