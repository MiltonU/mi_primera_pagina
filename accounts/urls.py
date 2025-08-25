from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ProfileView, InboxView, RegisterView, BoutiqueLoginView  # 👈 Importamos la vista boutique

app_name = 'accounts'

urlpatterns = [
    # 👤 Perfil sensorial del usuario
    path('profile/', ProfileView.as_view(), name='profile'),

    # 💬 Bandeja de entrada boutique
    path('', InboxView.as_view(), name='inbox'),

    # 🔐 Login y logout con templates personalizados
    path('login/', BoutiqueLoginView.as_view(), name='login'),  # 👈 Usamos la vista que redirige si ya está logueado
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # 📝 Registro de nuevos usuarios
    path('registro/', RegisterView.as_view(), name='register'),
]