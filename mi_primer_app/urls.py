from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # 🏠 Inicio (verificación incluida en home)
    path('', views.home, name='home'),
    path('acceso-denegado/', views.rechazo, name='rechazo'),

    # 🔐 Autenticación
    path('login/', views.mostrar_login, name='mostrar_login'),
    path('registro/', views.registro_usuario, name='registro'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),

    # 📥 Ingreso de datos
    path('formulario/', views.crear_objetos, name='formulario'),

    # 🔍 Búsqueda
    path('buscar/', views.buscar_vinos, name='buscar_vinos'),
]
