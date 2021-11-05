from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "Batata/index.html")

def gato1(request):
    return render(request, "Batata/gato1.html")

def gato2(request):
    return render(request, "Batata/gato2.html")
