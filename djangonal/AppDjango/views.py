from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'AppDjango/appdjango.html')

def quadrado(request):
    return render(request, 'AppDjango/quadrado.html')

def circulo(request):
    return render(request, 'AppDjango/circulo.html')

def triangulo(request):
    return render(request, 'AppDjango/triangulo.html')
