from django.urls import path, include
from app_fgv import views 

urlpatterns =[
    path('', views.index, name='index'),
    path('mypage/', views.mypage, name = 'mypage')
]