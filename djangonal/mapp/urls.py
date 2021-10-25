from django.urls import path, include
from mapp import views

urlpatterns = [
    path('', views.index, name = 'index')
]