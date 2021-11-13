from django.urls import path
from mapp import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('redirect/', views.redirect, name = 'redirect'),
    path('especial/<int:param>', views.especial_int, name = 'especial_int'),
    path('especial/<str:param>', views.especial_str, name = 'especial_str'),
    path('nada/', views.nada, name = 'nada'),
    path('quadro/', views.quadro, name = 'quadro_default'),
    path('quadro/<str:nome>', views.quadro, name = 'quadro'),
    path('sono/', views.sono, name = 'sono'),
    path('registrar/<str:nome>/<int:cr>', views.registrar, name = 'registrar')
]