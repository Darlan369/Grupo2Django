from django.urls import path
from Aquarela import views

urlpatterns = [
    path("", views.index, name ="index"),
    path("index/", views.index, name ="index"),
    path("especial/<int:param>", views.especial, name="especial"),
    path("redireciona/", views.redireciona, name="redireciona")
]
