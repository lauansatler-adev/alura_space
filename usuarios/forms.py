""" Representa os formulários da aplicação """

""" ## Importa o módulo de formulário do django permitindo criar e gerenciar formulários html em python
    *Transforma classes python em elementos visuais de formulário (como caixas de texto e botões)
    *Verifica de forma automática se o que o ultilizador digitou cumpre as regras definidas (como e-mails válidos ou campos obrigatórios)
    *Ajuda a proteger a aplicação contra ataques comuns, commo o CSRF(Cross-Site Request Forgery)
"""
from django import forms ##

class LoginForms(forms.Form): # Cria formulários gerais e independentes de bases de dados (como páginas de contacto ou de início de sessão)
    
    nome_login = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Lauan Satler"
            }
        )
    )
    
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(# Para dizer que é um campo de senha
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        ) 
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de Cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Lauan Satler"
            }
        )
    )
    
    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(# Para dizer que é um campo de email
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: lauansatler@xpto.com"
            }
        )
    )
    
    senha_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(# Para dizer que é um campo de senha
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        ) 
    )
    senha_2 = forms.CharField(
        label="Confirme sua senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(# Para dizer que é um campo de senha
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )
    