from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<strong>App Django</strong>")

def special(request):
    return render(request, 'appdjango.html')
