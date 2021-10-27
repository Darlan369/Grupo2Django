from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('<h2>Funcionou</h2>')

def special(request):
    return render(request, 'mapp.html')
