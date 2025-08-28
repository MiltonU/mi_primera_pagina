from django.shortcuts import render, redirect, get_object_or_404
from pages.models import Vino

def agregar_al_carrito(request, slug):
    vino = get_object_or_404(Vino, slug=slug)
    carrito = request.session.get('carrito', {})

    if slug not in carrito:
        carrito[slug] = {
            'nombre': vino.nombre,
            'precio': float(vino.precio),
            'imagen': vino.imagen.url if vino.imagen else '',
            'cantidad': 1
        }
    else:
        carrito[slug]['cantidad'] += 1

    request.session['carrito'] = carrito
    return redirect('carrito:ver')

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    total = sum(item['precio'] * item['cantidad'] for item in carrito.values())
    return render(request, 'carrito/carrito.html', {
        'carrito': carrito,
        'total': total
    })

def quitar_del_carrito(request, slug):
    carrito = request.session.get('carrito', {})
    if slug in carrito:
        del carrito[slug]
        request.session['carrito'] = carrito
    return redirect('carrito:ver')

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from carrito.models import Pedido, ItemPedido

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class PedidoListView(LoginRequiredMixin, ListView):
    model = Pedido
    template_name = 'carrito/pedido_list.html'
    context_object_name = 'pedidos'
    paginate_by = 6
    extra_context = {
        'title': 'Mis pedidos sensoriales',
        'show_navbar': True
    }

    def get_queryset(self):
        return Pedido.objects.filter(usuario=self.request.user).order_by('-creado_en')

@login_required
def checkout(request):
    carrito = request.session.get('carrito', {})
    if not carrito:
        messages.warning(request, "Tu carrito está vacío.")
        return redirect('carrito:ver')

    pedido = Pedido.objects.create(usuario=request.user, total=0)
    total = 0

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

    pedido.total = total
    pedido.save()
    request.session['carrito'] = {}
    messages.success(request, "✅ Pedido confirmado con éxito.")
    return redirect('pages:vino_list')