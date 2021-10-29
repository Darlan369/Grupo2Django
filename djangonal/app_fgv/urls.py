from django.urls import path, include
from app_fgv import views 

urlpatterns =[
    path('', views.index, name='index'),
    path('preços/', views.precos, name = 'preços'),
    path('quantidades/', views.quantidades, name = 'quantidades'),
    path('produtos/', views.produtos, name = 'produtos')
]