from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms 
from django.contrib.auth.models import User # Importa a tabela de usuários que fica dentro do django
from django.contrib import auth # importa o sistema integrado de autenticação do Django, permitindo gerir utilizadores, logins, logouts e permissões.
from django.contrib import messages

def login(request):
    form = LoginForms()
    
    if request.method == "POST":
        form = LoginForms(request.POST)
        
        if form.is_valid():
            nome = form["nome_login"].value()
            senha = form["senha"].value()
            
        usuario = auth.authenticate( # Autentidca os dados de login do usuário
            request,
            username=nome,
            password=senha
        )
        
        if usuario is not None:
            auth.login(request, usuario) # Realiza o login do usuário
            messages.success(request, f"{nome} logado com sucesso!")
            return redirect("index")
        
        else:
            messages.error(request, "Erro ao efetuar login")
            return redirect("login")  
    
    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()
    
    if request.method == "POST":
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            
            """ Pegando as informações passadas e colocando dentrode variáveis para organizar o código"""
            nome = form["nome_cadastro"].value()
            email = form["email"].value()
            senha = form["senha_1"].value()
            
            if User.objects.filter(username=nome).exists(): # Verifica se já existe um usuário com esse nome na tabela do django
                messages.error(request, "Usuário ja existente")
                return redirect("cadastro") # Retornando para a página de cadastro caso já exista um usuário com esse nome
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            ) # Criando um usuário com as informações passadas na página de cadastro
            
            usuario.save() # Salvando o usuário no banco de dados
            
            messages.success(request, "Cadastro efetuado com sucesso")
            return redirect("login") # Redireciona para a página de login se todos os dados estiverem corretos
        
    return render(request, "usuarios/cadastro.html", {"form": form})

def logout(request):
    
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    
    return redirect("login")
    