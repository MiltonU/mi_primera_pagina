from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import EditarPerfilView
from .views import (
    ProfileView,
    InboxView,
    RegisterView,
    BoutiqueLoginView,
    
)

app_name = 'accounts'

urlpatterns = [
    # 👤 Perfil sensorial del usuario
    path('profile/', ProfileView.as_view(), name='profile'),

    # 💬 Bandeja de entrada boutique
    path('', InboxView.as_view(), name='inbox'),

    # 🔐 Login con redirección si ya está logueado
    path('login/', BoutiqueLoginView.as_view(), name='login'),

    # 🔓 Logout con redirección al home boutique
    path('logout/', LogoutView.as_view(next_page='pages:vino_list'), name='logout'),

    # 📝 Registro de nuevos usuarios
    path('registro/', RegisterView.as_view(), name='register'),

    path('editar/', EditarPerfilView.as_view(), name='editar_perfil'),
]
