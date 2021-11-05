from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http.response import HttpResponseNotFound, HttpResponseRedirect

def index(request):
    return render(request, "Batata/index.html")

def gato1(request, Tomate):
    if Tomate == 1:
        return render(request, "Batata/gato1.html")
    else:
        return render(request, "Batata/gato2.html")

def gato2(request, Ovo):
    Dicionario = {

        'Criativo': Ovo

    }
    return render(request, "Batata/gato2.html", Dicionario)

def redireciona(request):
    r = reverse('gato1', args=['1'])
    return HttpResponseRedirect(r)
