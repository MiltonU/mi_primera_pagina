from django.urls import path
from . import views

app_name = 'carrito'

urlpatterns = [
    path('', views.ver_carrito, name='ver'),
    path('agregar/<slug:slug>/', views.agregar_al_carrito, name='agregar'),
    path('quitar/<slug:slug>/', views.quitar_del_carrito, name='quitar'),
]