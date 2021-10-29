from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'app_fgv/app_fgv.html')

def precos(request):
    return render(request, 'app_fgv/preços.html')

def quantidades(request):
    return render(request, 'app_fgv/quantidades.html')

def produtos(request):
    return render(request, 'app_fgv/produtos.html')