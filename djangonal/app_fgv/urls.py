from django.urls import path, include
from app_fgv import views 

urlpatterns =[
    path('app_fgv', views.app_fgv, name='app_fgv'),
    path('redireciona/', views.redireciona, name = 'redireciona'),
    path('preços/<int:param1>', views.preços, name = 'preços'),
    path('quantidades/<int:param2>', views.quantidades, name = 'quantidades'),
    path('produtos/', views.produtos, name = 'produtos'),
    path('registrar/<str:nome>/<int:quantidade>/<int:preço>', views.registrar, name = 'registrar'),
    
]