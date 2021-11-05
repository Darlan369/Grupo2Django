from django.urls import path

from luca import views

urlpatterns = [
    path("", views.index, name="index"),
    path("luca/", views.luca, name="luca"),
    path("special/<int:param>", views.special, name="special"),
    path("redireciona/", views.redir, name="redireciona")

]