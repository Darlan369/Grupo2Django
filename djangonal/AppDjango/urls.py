from django.urls import path
from AppDjango import views as app_views

urlpatterns = [
    path("", app_views.index, name ="index"),
    path("index/", app_views.index, name ="index"),
]
