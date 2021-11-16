from django.http import HttpResponse
from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from app_fgv.models import Produto
from datetime import date

def app_fgv(request):
    return render(request,'app_fgv/app_fgv.html')


def produtos(request):
    lista_de_produtos = ["chocolate", "balinha", "maçã"]

    context = {
        "produtos":lista_de_produtos,
        'data': date.fromisoformat('2021-12-25')
    }

    return render(request, 'app_fgv/produtos.html',context)



def registrar(request, nome, quantidade, preço):
    produto = Produto(nome = nome.capitalize(), quantidade = quantidade, preço= preço)
    produto.save()
    context = {'nome': nome.capitalize(),
                'quantidade' : quantidade , 
                "preço": preço }
    return render(request, 'app_fgv/registro.html', context)






def preços(request, param1):
    lista_de_produtos = ["chocolate", "balinha", "maçã"]
    lista_preco =[10, 2, 7]
    
    if param1 == 1:
        idx = param1 -1
    elif param1 == 2:
        idx = param1 -1
    elif param1 == 2:
        idx = param1 -1
    else:
        raise Http404()

    context = {
        "param1":lista_de_produtos[idx],
        "preço": lista_preco[idx]
    }

    return render(request, "app_fgv/preços.html", context)

def quantidades(request, param2):
    lista_de_produtos = ["chocolate", "balinha", "maçã"]
    lista_quantidades = [1, 1000, 70]

    if param2 == 1:
        idx = param2 -1
    elif param2 == 2:
        idx = param2 -1
    elif param2 == 2:
        idx = param2 -1
    else:
        raise Http404()

    

    context = {
        "param2": lista_de_produtos[idx],
        "quantidade": lista_quantidades[idx]

    }

    return render(request, "app_fgv/quantidades.html", context)

def redireciona(request):
    url_redirecionamento = reverse("app_fgv")
    return HttpResponseRedirect(url_redirecionamento)