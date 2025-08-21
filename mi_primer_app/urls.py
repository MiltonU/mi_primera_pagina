from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    # Verificación de edad
    path('verificar_edad/', views.verificar_edad, name='verificar_edad'),

    # Registro de usuario
    path('registro/', views.registro_usuario, name='registro'),

    # Login nativo con template boutique
    path('login/', views.CustomLoginView.as_view(), name='login'),

    # Logout (opcional, usando vista nativa)
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Formulario para agregar vino
    path('agregar/', views.agregar_vino, name='agregar_vino'),

    # Comprar vino
    path('comprar/<int:vino_id>/', views.comprar_vino, name='comprar_vino'),

    # Buscar vino
    path('buscar/', views.buscar_vino, name='buscar_vino'),
]

