from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request, 'home.html')

def clientes(request):
    return render (request, 'clientes.html')

def licencas(request):
    return render (request, 'licencas.html')

def painel(request):
    return render (request, 'painel.html')