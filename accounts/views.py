from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# 👤 Vista sensorial del perfil de usuario
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
    extra_context = {
        'title': 'Perfil de Usuario',
        'subtitle': 'Tu espacio personal boutique'
    }

# 💬 Vista de bandeja de entrada (mensajería interna)
class InboxView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/inbox.html'
    extra_context = {
        'title': 'Mensajes',
        'subtitle': 'Tu bandeja sensorial'
    }