from django.urls import path
from AppDjango import views

urlpatterns = [
    path("", views.index, name ="index"),
    path("quadrado/", views.quadrado, name ="quadrdado"),
    path("circulo/", views.circulo, name ="circulo"),
    path("triangulo/", views.triangulo, name ="triangulo"),
    path('redireciona/', views.redireciona, name = 'redireciona'),
    path('special/<int:param>', views.dinamica_int, name = 'dinamica_int'),
    path('special/<str:param>', views.dinamica_str, name = 'dinamica_str'),
    path('dtl/', views.special_dtl, name='retorna_html_dtl'),
]
