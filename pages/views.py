from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from .models import Page, Vino

# 🍷 Vistas sensoriales para el modelo Vino

class VinoListView(ListView):
    model = Vino
    template_name = 'pages/vino_list.html'
    context_object_name = 'vinos'
    extra_context = {'title': 'Selección Boutique'}

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('mayor_edad'):
            return redirect('home')  # o 'verificar_edad' si lo separás
        return super().dispatch(request, *args, **kwargs)
    
class VinoDetailView(DetailView):
    model = Vino
    template_name = 'pages/vino_detail.html'
    extra_context = {'title': 'Ficha de Vino'}

class VinoCreateView(LoginRequiredMixin, CreateView):
    model = Vino
    fields = ['nombre', 'varietal', 'añada', 'notas', 'maridaje', 'imagen', 'slug']
    template_name = 'pages/vino_form.html'
    success_url = reverse_lazy('pages:vino_list')
    extra_context = {'title': 'Nuevo Vino'}

class VinoUpdateView(LoginRequiredMixin, UpdateView):
    model = Vino
    fields = ['nombre', 'varietal', 'añada', 'notas', 'maridaje', 'imagen', 'slug']
    template_name = 'pages/vino_form.html'
    success_url = reverse_lazy('pages:vino_list')
    extra_context = {'title': 'Editar Vino'}

class VinoDeleteView(LoginRequiredMixin, DeleteView):
    model = Vino
    template_name = 'pages/vino_confirm_delete.html'
    success_url = reverse_lazy('pages:vino_list')
    extra_context = {'title': 'Eliminar Vino'}

# 📄 Vistas narrativas para el modelo Page

class PageListView(LoginRequiredMixin, ListView):
    model = Page
    template_name = 'pages/page_list.html'
    context_object_name = 'pages'
    paginate_by = 6
    extra_context = {'title': 'Mis Publicaciones'}

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Page.objects.filter(author=self.request.user).order_by('-created_at')
        return Page.objects.none()

class PageDetailView(LoginRequiredMixin, DetailView):
    model = Page
    template_name = 'pages/page_detail.html'
    context_object_name = 'page'
    extra_context = {'title': 'Detalle de Publicación'}

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    template_name = 'pages/page_form.html'
    fields = ['title', 'content', 'image']
    success_url = reverse_lazy('pages:page_list')
    extra_context = {'title': 'Nueva Publicación'}

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    template_name = 'pages/page_form.html'
    fields = ['title', 'content', 'image']
    success_url = reverse_lazy('pages:page_list')
    extra_context = {'title': 'Editar Publicación'}

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('pages:page_list')
    extra_context = {'title': 'Eliminar Publicación'}