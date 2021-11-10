from django.urls import path
from AppDjango import views

urlpatterns = [
    path("", views.index, name ="index"),
    path("quadrado/", views.quadrado, name ="quadrdado"),
    path("circulo/", views.circulo, name ="circulo"),
    path("triangulo/", views.triangulo, name ="triangulo"),
]
