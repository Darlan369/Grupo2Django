from django.urls import path,include
from AppDjango import views as app_views

urlpatterns = [
    path("", app_views.AppDjango, name='AppDjango'),
    path(r"AppDjango/", include("AppDjango.urls"))
]
