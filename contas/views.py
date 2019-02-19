from django.shortcuts import render, HttpResponse

# Create your views here.

def paginaInicial(request):
    return HttpResponse('Bem vindo a página do app de contas')

def login(request):
    return HttpResponse('Pagina de Login')

def registro(request):
    return HttpResponse('Pagina de Registro')
