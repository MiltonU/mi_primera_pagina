from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_vino, name='agregar_vino'),
    path('comprar/<int:vino_id>/', views.comprar_vino, name='comprar_vino'),
    path('home/', views.home, name='home'),
    
]


