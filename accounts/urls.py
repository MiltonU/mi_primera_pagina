from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ProfileView, InboxView, RegisterView

app_name = 'accounts'

urlpatterns = [
    # 👤 Perfil sensorial del usuario
    path('profile/', ProfileView.as_view(), name='profile'),

    # 💬 Bandeja de entrada boutique
    path('', InboxView.as_view(), name='inbox'),

    # 🔐 Login y logout con templates personalizados
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # 📝 Registro de nuevos usuarios
    path('registro/', RegisterView.as_view(), name='register'),
]