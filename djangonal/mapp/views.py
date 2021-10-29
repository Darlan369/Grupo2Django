from django.http import HttpResponse
from django.shortcuts import render

def nada(request):
    return HttpResponse('<h2>Não tem nada aqui</h2>')

def index(request):
    return render(request, 'mapp/index.html')

def quadro(request):
    return render(request, 'mapp/quadro.html')

def sono(request):
    return render(request, 'mapp/sono.html')