from django.http import HttpResponse

# Create your views here.

def luca(request):
    return HttpResponse("<strong>Luca Lindo!!</strong>")