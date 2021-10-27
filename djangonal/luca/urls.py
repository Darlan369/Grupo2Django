from django.urls import path

from luca import views as luca_views

urlpatterns = [
    path("", luca_views.luca, name="luca")
]