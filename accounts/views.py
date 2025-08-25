from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.auth import get_user_model
from .models import Profile
from messenger.models import Message  # Asegurate de que el modelo se llame exactamente así

User = get_user_model()

# 👤 Vista sensorial del perfil de usuario
class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile.html'
    context_object_name = 'profile'
    extra_context = {
        'title': 'Perfil de Usuario',
        'subtitle': 'Tu espacio personal boutique'
    }

    def get_object(self):
        return self.request.user.profile

# 💬 Vista de bandeja de entrada (mensajería interna)
class InboxView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'accounts/inbox.html'
    context_object_name = 'mensajes'
    extra_context = {
        'title': 'Mensajes',
        'subtitle': 'Tu bandeja sensorial'
    }

    def get_queryset(self):
        return Message.objects.filter(recipient=self.request.user).order_by('-sent_at')

# 🧾 Vista de historial de actividad (opcional, para escalar)
class ActivityLogView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/activity_log.html'
    extra_context = {
        'title': 'Historial',
        'subtitle': 'Tu rastro editorial'
    }

# ⚙️ Vista de configuración de cuenta (opcional)
class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/settings.html'
    extra_context = {
        'title': 'Configuración',
        'subtitle': 'Ajustes sensoriales de tu cuenta'
    }