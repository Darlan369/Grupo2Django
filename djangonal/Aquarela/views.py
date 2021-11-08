from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

#def index(request):
#    return HttpResponse("<strong>Aquarela</strong>")

def index(request):
    return render(request, "Aquarela/Aquarela.html")

def especial(request, param):
    cores = ["vERMElho", "veRde", "AZul", "amARelo", "maRROm"]
    contexto = {"parametro": param, "cores":cores}
    if param % 2 == 0:
        return render(request, "Aquarela/Aquarela_0.html", contexto)
    elif param % 2 == 1:
        return render(request, "Aquarela/Aquarela_1.html", contexto)
    else: 
        return HttpResponseNotFound("<strong>Página não esncontrada!!!</strong>")

def redireciona(request):
    direcionamento = reverse('Aquarela')
    return HttpResponseRedirect(direcionamento)
