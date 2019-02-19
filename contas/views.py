from django.shortcuts import render, HttpResponse

# Create your views here.

def paginaInicial(request):
    descricao = 'Uma descricao dinamica'
    numero = 20 + 30
    return render(request, "contas/home.html", {'descricao':descricao, 'num': numero})

def login(request):
    return render(request, "contas/login.html")

def registro(request):
    return HttpResponse('Pagina de Registro')
