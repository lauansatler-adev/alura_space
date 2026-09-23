""" Responsável pelas ROTAS da app usuarios"""
from django.urls import path # Usado para mapear endereços web (URLs) para funcções de visualização (views)
from usuarios.views import login, cadastro

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro')
]