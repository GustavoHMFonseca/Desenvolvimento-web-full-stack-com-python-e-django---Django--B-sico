from django.shortcuts import render
"""
Tem os recursos para fazer a exibição
utilizando o html e css(template)
"""
# Create your views here.

from django.http import HttpResponse


def index(request):
    # processamento, banco de dados
    context = {
        'nome': 'Gustavo Fonseca',
        'ultimo_acesso': '10/10/2030',
        'idade':15,
        'produtos': [
            {'nome': 'Notebook Acer', 'preco': '1.200,00'},
            {'nome': 'Iphone', 'preco': '2.200,00'},
            {'nome': 'Samsung', 'preco': '4.200,00'},
        ]
    }
    return render(request, 'index.html',context)


def celulares(request):
    return render(request, 'celulares.html')
