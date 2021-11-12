from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
import random


def index(request):
    return render(request, "Batata/index.html")

def gato1(request, Tomate):
    if Tomate == 1:
        return render(request, "Batata/gato1.html")
    else:
        return render(request, "Batata/gato2.html")

def gato2(request, Ovo):

    if Ovo == 'omelete':
        omelete = 'Gosta de omelete?'
    else:
        omelete = ''

    Listas = ['Batata', 'Tomate', 'Maçã', 'Pera', 'Gnomio', 'Apricorno', 'Uva', 'Abóbora', 'Laranja', 'Manga']
    Lista = []

    for fruta in Listas:
        if len(fruta) == 6:
            Lista.append(fruta)

    if random.randint(0, 1) == 0:
        Gato = "Cara preta é fofa"
    else:
        Gato = "Espuleta é fofo"



    Dicionario = {

        'Criativo': Ovo,
        'Omelete': omelete,
        'Lista': Lista,
        'Gato': Gato

    }
    return render(request, "Batata/gato2.html", Dicionario)

def redireciona(request):
    r = reverse('gato1', args=['1'])
    return HttpResponseRedirect(r)
