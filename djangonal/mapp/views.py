from django.http import HttpResponse
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import random

def nada(request):
    return HttpResponse('<h2>Não tem nada aqui</h2>')

def index(request):
    return render(request, 'mapp/index.html')

def quadro(request, param1 = 'Marcelo'):
    context = {
        'nome': param1,
        'number': random.randint(0,100)
    }
    return render(request, 'mapp/quadro.html', context)

def sono(request):
    return render(request, 'mapp/sono.html')

def especial_int(request, param):
    if param == 0:
        return HttpResponse('<h2>Parâmetro de valor 0</h2> <h4>Não natural para alguns</h4>')
    elif param % 2 == 0:
        return HttpResponse('<h2>Parâmetro de valor par</h2>')
    elif param % 2 == 1:
        return HttpResponse('<h2>Parâmetro de valor ímpar</h2>')
    else:
        return HttpResponseNotFound('Página não existe.')

def especial_str(request, param):
    if param == 'vazio':
        return HttpResponse('<h2>Você estuda cálculo<h2>')
    elif param == 'dor':
        return HttpResponse('<h2>Você estuda álgebra linear</h2>')
    else:
        return HttpResponseNotFound('Página não existe.')

def redireciona(request):
    # return HttpResponseRedirect('mapp/especial/vazio')
    url_redirecionamento = reverse('especial_str', args = ['vazio'])
    return HttpResponseRedirect(url_redirecionamento)
