from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, TemplateView, FormView, View
from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.http import Http404
from .models import Profile
from .forms import UserForm, ProfileForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensajes_recibidos'] = Message.objects.filter(
            recipient=self.request.user
        ).order_by('-sent_at')[:5]  # Mostramos los 5 más recientes
        return context
    def get(self, request):
        profile, creado = Profile.objects.get_or_create(user=request.user)
        return render(request, 'accounts/profile.html', {
            'profile': profile
        })



# 🛠 Vista combinada para editar datos de usuario y perfil sensorial
class EditarPerfilView(LoginRequiredMixin, View):
    def get(self, request):
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        return render(request, 'accounts/editar_perfil.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })

    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('accounts:profile')

        return render(request, 'accounts/editar_perfil.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })

# 💬 Vista de bandeja de entrada (mensajería interna)
class InboxView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'messenger/inbox.html'
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

# 📝 Vista de registro boutique
class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:profile')  # Redirige al perfil sensorial

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

# 🔐 Vista de login con redirección si ya está autenticado
class BoutiqueLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True  # Evita mostrar login si ya está logueado

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('pages:vino_list'))  # Redirige a la home boutique
        return super().dispatch(request, *args, **kwargs)