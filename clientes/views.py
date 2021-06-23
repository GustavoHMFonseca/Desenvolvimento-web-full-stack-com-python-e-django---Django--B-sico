from django.shortcuts import render


def index(request):
    return render(request, 'clientes/index.html')


def email(request):
    return render(request, 'clientes/email.html')
