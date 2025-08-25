from django.urls import path
from .views import ProfileView, InboxView

app_name = 'accounts'

urlpatterns = [
    # 👤 Perfil sensorial del usuario
    path('profile/', ProfileView.as_view(), name='profile'),

    # 💬 Bandeja de entrada boutique
    path('', InboxView.as_view(), name='inbox'),
]