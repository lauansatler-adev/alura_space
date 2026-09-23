from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User # Importa a tabela de usuários que fica dentro do django

def login(request):
    
    form = LoginForms()
    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()
    
    if request.method == "POST":
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value(): #Verifica se as senhas são diferentes
                return redirect("cadastro") # Retornando para a página de cadastro caso as senhas sejam diferentes
            
            """ Pegando as informações passadas e colocando dentrode variáveis para organizar o código"""
            nome = form["nome_cadastro"].value()
            email = form["email"].value()
            senha = form["senha_1"].value()
            
            if User.objects.filter(username=nome).exists(): # Verifica se já existe um usuário com esse nome na tabela do django
                return redirect("cadastro") # Retornando para a página de cadastro caso já exista um usuário com esse nome
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            ) # Criando um usuário com as informações passadas na página de cadastro
            
            usuario.save() # Salvando o usuário no banco de dados
            
            return redirect("login") # Redireciona para a página de login se todos os dados estiverem corretos
        
    return render(request, "usuarios/cadastro.html", {"form": form})
