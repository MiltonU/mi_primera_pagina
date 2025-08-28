from django.urls import path
from carrito import views

app_name = 'carrito'

urlpatterns = [
    path('', views.ver_carrito, name='ver'),
    path('agregar/<slug:slug>/', views.agregar_al_carrito, name='agregar'),
    path('quitar/<slug:slug>/', views.quitar_del_carrito, name='quitar'),
    path('checkout/', views.checkout, name='checkout'),

    path('mis-pedidos/', views.PedidoListView.as_view(), name='mis_pedidos'),
]