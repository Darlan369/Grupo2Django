from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('<h2>Funcionou</h2>')
# Create your views here.
