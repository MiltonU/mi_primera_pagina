from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Page

# 🗂 Listado de páginas
class PageListView(LoginRequiredMixin, ListView):
    model = Page
    template_name = 'pages/page_list.html'
    context_object_name = 'pages'
    paginate_by = 6

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Page.objects.filter(author=self.request.user).order_by('-created_at')
        return Page.objects.none()

# 🔍 Detalle de una página
class PageDetailView(LoginRequiredMixin, DetailView):
    model = Page
    template_name = 'pages/page_detail.html'
    context_object_name = 'page'

# ➕ Crear nueva página
class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    template_name = 'pages/page_form.html'
    fields = ['title', 'content', 'image']  # Adaptá según tu modelo
    success_url = reverse_lazy('pages:page_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# ✏️ Editar página existente
class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    template_name = 'pages/page_form.html'
    fields = ['title', 'content', 'image']
    success_url = reverse_lazy('pages:page_list')

# 🗑 Eliminar página
class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('pages:page_list')