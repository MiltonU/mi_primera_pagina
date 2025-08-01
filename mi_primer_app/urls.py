from django.urls import path
from . import views

urlpatterns = [
    path('', views.hola_mundo, name='inicio'),
]
