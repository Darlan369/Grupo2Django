from django.urls import path
from Aquarela import views as Aquarela_views

urlpatterns = [
    path("", Aquarela_views.index, name ="index"),
    path("index/", Aquarela_views.index, name ="index"),
]
