from django.urls import path
from mapp import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('nada/', views.nada, name = 'nada'),
    path('quadro/', views.quadro, name = 'quadro'),
    path('sono/', views.sono, name = 'sono')
]