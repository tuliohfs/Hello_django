from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('Hello Word')

def soma(request, n1, n2):
    
    total = int(n1) + int(n2)
    return HttpResponse("A soma de {} e {} e igual {}".format(n1, n2, total))
    
def subtracao(request, n1, n2):
    
    total = int(n1) - int(n2)
    return HttpResponse("A Subtração de {} e {} e igual {}".format(n1, n2, total))

def multiplicacao(request, n1, n2):
    
    total = int(n1) * int(n2)
    return HttpResponse("A Multiplicação de {} e {} e igual {}".format(n1, n2, total))

def divisao(request, n1, n2):
    
    total = int(n1) / int(n2)
    return HttpResponse("A Divisão de {} e {} e igual {}".format(n1, n2, total))