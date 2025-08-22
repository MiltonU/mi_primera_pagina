from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from .models import Page, Vino

# 🧩 Vistas para el modelo Vino

class VinoListView(ListView):
    model = Vino
    template_name = 'pages/vino_list.html'
    context_object_name = 'vinos'


class VinoDetailView(DetailView):
    model = Vino
    template_name = 'pages/vino_detail.html'

class VinoCreateView(LoginRequiredMixin, CreateView):
    model = Vino
    fields = ['nombre', 'varietal', 'añada', 'notas', 'maridaje', 'imagen', 'slug']
    template_name = 'pages/vino_form.html'
    success_url = reverse_lazy('pages:vino_list')

class VinoUpdateView(LoginRequiredMixin, UpdateView):
    model = Vino
    fields = ['nombre', 'varietal', 'añada', 'notas', 'maridaje', 'imagen', 'slug']
    template_name = 'pages/vino_form.html'
    success_url = reverse_lazy('pages:vino_list')

class VinoDeleteView(LoginRequiredMixin, DeleteView):
    model = Vino
    template_name = 'pages/vino_confirm_delete.html'
    success_url = reverse_lazy('pages:vino_list')

# 🧩 Vistas para el modelo Page

class PageListView(LoginRequiredMixin, ListView):
    model = Page
    template_name = 'pages/page_list.html'
    context_object_name = 'pages'
    paginate_by = 6

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Page.objects.filter(author=self.request.user).order_by('-created_at')
        return Page.objects.none()

class PageDetailView(LoginRequiredMixin, DetailView):
    model = Page
    template_name = 'pages/page_detail.html'
    context_object_name = 'page'

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    template_name = 'pages/page_form.html'
    fields = ['title', 'content', 'image']
    success_url = reverse_lazy('pages:page_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    template_name = 'pages/page_form.html'
    fields = ['title', 'content', 'image']
    success_url = reverse_lazy('pages:page_list')

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('pages:page_list')

# 🧩 Vista basada en función (decorador aplicado)
def page_detail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'pages/page_detail.html', {'page': page})