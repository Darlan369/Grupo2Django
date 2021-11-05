from django.urls import path
from mapp import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('redireciona/', views.redireciona, name = 'redirecionada'),
    path('especial/<int:param>', views.especial_int, name = 'especial_int'),
    path('especial/<str:param>', views.especial_str, name = 'especial_str'),
    path('nada/', views.nada, name = 'nada'),
    path('quadro/<str:param1>', views.quadro, name = 'quadro'),
    path('sono/', views.sono, name = 'sono'),
]