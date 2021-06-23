from django.shortcuts import render
"""
Tem os recursos para fazer a exibição
utilizando o html e css(template)
"""
# Create your views here.

from django.http import HttpResponse


def pagina_produtos(request):
    return HttpResponse('Página de produtos')


def celulares(request):
    return HttpResponse('Página de celulares')
