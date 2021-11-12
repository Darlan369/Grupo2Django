from django.http import HttpResponse
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

def index(request):
    return render(request, 'AppDjango/appdjango.html')

def quadrado(request):
    return render(request, 'AppDjango/quadrado.html')

def circulo(request):
    return render(request, 'AppDjango/circulo.html')

def triangulo(request):
    return render(request, 'AppDjango/triangulo.html')


def dinamica_int(request, param):
    if param == 0:
        return render(request, "AppDjango/circulo.html")
    elif param == 1:
        return render(request, "AppDjango/triangulo.html")
    elif param == 2:
        return render(request, "AppDjango/circulo.html")
    else: 
        return HttpResponseNotFound('Página não existe.')

def dinamica_str(request, param):
    if param == 'velho':
        return HttpResponse('<h2>Você escuta Britney Spears<h2>')
    elif param == 'novo':
        return HttpResponse('<h2>Você escuta BLACKPINK</h2>')
    else:
        return HttpResponseNotFound('Página não existe.')

def redireciona(request):
    url_redirecionamento = reverse('dinamica_str', args=['novo'])
    return HttpResponseRedirect(url_redirecionamento)