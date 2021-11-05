from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("<strong>Luca Lindo!!</strong>")

def luca(request):
    return render(request, 'luca/luca.html')

def special(request, param):
    if param%2 == 0:
        paridade = "par"

    else:
        paridade = "ímpar"

    context = {
        "param": param,
        "paridade": paridade
    }

    return render(request, "luca/paridade.html", context)

def redir(request):
    direcionamento = reverse("luca")
    return HttpResponseRedirect(direcionamento)