from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from mapp.models import Aluno
from datetime import date
from random import randint

def nada(request):
    return HttpResponse('<h2>Não tem nada aqui</h2>')

def index(request):
    return render(request, 'mapp/index.html')

def quadro(request, nome = 'marcelo'):
    context = {
        'name': nome,
        'number': randint(0,101),
        'filters': ['timeuntil', False, 'urlize'],
        'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        'date': date.fromisoformat('2022-02-04')
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
        raise Http404()

def redirect(request):
    # return HttpResponseRedirect('mapp/especial/vazio')
    url_redirecionamento = reverse('especial_str', args = ['vazio'])
    return HttpResponseRedirect(url_redirecionamento)

def registrar(request, nome, cr):
    aluno = Aluno(nome = nome.capitalize(), cr = cr)
    aluno.save()
    context = {'nome': nome.capitalize(), 'cr': cr}
    return render(request, 'mapp/registro.html', context)
