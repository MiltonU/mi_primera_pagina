from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Page, Vino
from django.views.generic import TemplateView
from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from carrito.models import Pedido, ItemPedido
from pages.models import Vino
from messenger.models import Message
from django.contrib.auth.models import User

@login_required
def checkout(request):
    carrito = request.session.get('carrito', {})

    if request.method == 'POST':
        if not carrito:
            messages.warning(request, "Tu carrito está vacío.")
            return redirect('carrito:ver')

        pedido = Pedido.objects.create(usuario=request.user, total=0)
        total = 0
        resumen = []

        for slug, item in carrito.items():
            vino = get_object_or_404(Vino, slug=slug)
            cantidad = item['cantidad']
            precio_unitario = vino.precio
            subtotal = cantidad * precio_unitario

            ItemPedido.objects.create(
                pedido=pedido,
                producto=vino,
                cantidad=cantidad,
                precio_unitario=precio_unitario
            )

            total += subtotal
            resumen.append(f"- {cantidad} × {vino.nombre} (${subtotal:.2f})")

        pedido.total = total
        pedido.save()
        request.session['carrito'] = {}

        # Mensaje interno con resumen sensorial
        sistema = User.objects.filter(is_superuser=True).first()
        if sistema:
            Message.objects.create(
                sender=sistema,
                recipient=request.user,
                subject="🧾 Confirmación de pedido",
                body=f"""
Hola {request.user.first_name or request.user.username},

Tu pedido #{pedido.id} fue confirmado con éxito el {pedido.creado_en.strftime('%d/%m/%Y %H:%M')}.
Total: ${pedido.total:.2f}

Detalle sensorial:
{chr(10).join(resumen)}

Gracias por confiar en nuestra experiencia boutique.
""".strip()
            )

        messages.success(request, "✅ Pedido confirmado con éxito.")
        return redirect('carrito:mis_pedidos')

    # Si es GET, mostrar el resumen
    items = []
    total = 0
    for slug, item in carrito.items():
        vino = get_object_or_404(Vino, slug=slug)
        cantidad = item['cantidad']
        subtotal = vino.precio * cantidad
        total += subtotal
        items.append({
            'vino': vino,
            'cantidad': cantidad,
            'subtotal': subtotal
        })

    return render(request, 'carrito/checkout.html', {
        'items': items,
        'total': total
    })

class ContactView(TemplateView):
    template_name = 'pages/contact.html'
    extra_context = {
        'title': 'Contacto',
        'show_navbar': True
    }

class AboutView(TemplateView):
    template_name = 'pages/about.html'
    extra_context = {
        'title': 'Sobre mí',
        'show_navbar': True,  # Cambiá a False si querés una vista más íntima
        'description': 'Este proyecto nace de la obsesión por la modularidad, la estética editorial y la experiencia de usuario premium. Cada vista, cada template, respira intención y atmósfera.'
    }


# 🍷 Vistas sensoriales para el modelo Vino

class VinoListView(ListView):
    model = Vino
    template_name = 'pages/vino_list.html'
    context_object_name = 'vinos'
    extra_context = {'title': 'Selección Boutique'}

    def get_queryset(self):
        qs = Vino.objects.all()
        varietal = self.request.GET.get("varietal")
        precio_max = self.request.GET.get("precio_max")
        añada = self.request.GET.get("añada")

        if varietal:
            qs = qs.filter(varietal__icontains=varietal)
        if precio_max:
            qs = qs.filter(precio__lte=precio_max)
        if añada:
            qs = qs.filter(añada__year=añada)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_navbar'] = True
        context['varietal'] = self.request.GET.get("varietal", "")
        context['precio_max'] = self.request.GET.get("precio_max", "")
        context['añada'] = self.request.GET.get("añada", "")
        return context

class VinoDetailView(DetailView):
    model = Vino
    template_name = 'pages/vino_detail.html'
    extra_context = {
        'title': 'Ficha de Vino',
        'show_navbar': False
    }

class VinoCreateView(LoginRequiredMixin, CreateView):
    model = Vino
    fields = ['nombre', 'varietal', 'añada', 'precio', 'notas', 'maridaje', 'imagen', 'slug']
    template_name = 'pages/vino_form.html'
    success_url = reverse_lazy('pages:vino_list')
    extra_context = {
        'title': 'Nuevo Vino',
        'show_navbar': False
    }

class VinoUpdateView(LoginRequiredMixin, UpdateView):
    model = Vino
    fields = ['nombre', 'varietal', 'añada', 'precio', 'notas', 'maridaje', 'imagen', 'slug']
    template_name = 'pages/vino_form.html'
    success_url = reverse_lazy('pages:vino_list')
    extra_context = {
        'title': 'Editar Vino',
        'show_navbar': False
    }

class VinoDeleteView(LoginRequiredMixin, DeleteView):
    model = Vino
    template_name = 'pages/vino_confirm_delete.html'
    success_url = reverse_lazy('pages:vino_list')
    extra_context = {
        'title': 'Eliminar Vino',
        'show_navbar': False
    }

# 📄 Vistas narrativas para el modelo Page

class PageListView(LoginRequiredMixin, ListView):
    model = Page
    template_name = 'pages/page_list.html'
    context_object_name = 'page_list'
    paginate_by = 6
    extra_context = {
        'title': 'Mis Publicaciones',
        'show_navbar': False
    }

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Page.objects.filter(author=self.request.user).order_by('-created_at')
        return Page.objects.none()

class PageDetailView(LoginRequiredMixin, DetailView):
    model = Page
    template_name = 'pages/page_detail.html'
    context_object_name = 'page'
    extra_context = {
        'title': 'Detalle de Publicación',
        'show_navbar': False
    }


class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ['title', 'subtitle', 'content', 'image']
    template_name = 'pages/page_form.html'
    success_url = reverse_lazy('pages:page_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        print("✅ Página lista para guardar:", form.cleaned_data)
        messages.success(self.request, "✅ Página creada con éxito.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "⚠️ No se pudo crear la página. Revisá los campos.")
        return super().form_invalid(form)

    
from django.views.generic.edit import UpdateView

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ['title', 'subtitle', 'content', 'image']
    template_name = 'pages/page_form.html'
    success_url = '/pages/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "✅ Página actualizada con éxito.")
        return super().form_valid(form)


    def get_queryset(self):
        return Page.objects.filter(author=self.request.user)

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('pages:page_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "🗑️ Página eliminada correctamente.")
        return super().delete(request, *args, **kwargs)


    def get_queryset(self):
        return Page.objects.filter(author=self.request.user)
    
