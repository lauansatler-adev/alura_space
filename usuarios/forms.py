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
    
    """ Método que permite fazer a validação dos nomes cadastrados
        Precisa começar com "clean" acompanhado com o nome do campo do formulário
        que é preciso validar, pois o django interpreta dessa forma
    """
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro") #Pega as informações passadas em nome_cadastro
        
        if nome:
            nome = nome.strip() # Tira os espaços no inicio e no fim da string
            if " " in nome:
                raise forms.ValidationError("Espaços não são permitidos nesse campo") #Erro caso exista espaço na string
            else:
                return nome
            
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get("senha_1") #Recebe a senha 1
        senha_2 = self.cleaned_data.get("senha_2") #Recebe a senha 2
        
        if senha_1 and senha_2: # Verifica se as senhas existem
            if senha_1 != senha_2: # Compara se elas são diferentes
                raise forms.ValidationError("Senhas não são iguais") #Retorna mensagem de erro
            else:
                return senha_2