
from django.urls import path
from Batata import views
urlpatterns = [
    path('gato1/<int:Tomate>', views.gato1, name='gato1'),
    path('gato2/<str:Ovo>', views.gato2, name='gato2'),
    path('index/', views.index, name='index'),
    path('redireciona/', views.redireciona, name='redireciona')

]



