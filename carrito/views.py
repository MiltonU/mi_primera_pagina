from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from pages.models import Vino
from carrito.models import Pedido, ItemPedido
from messenger.models import Message  # Modelo correcto

# Agregar producto al carrito
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

# Ver contenido del carrito
def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    total = sum(item['precio'] * item['cantidad'] for item in carrito.values())
    return render(request, 'carrito/carrito.html', {
        'carrito': carrito,
        'total': total
    })

# Quitar producto del carrito
def quitar_del_carrito(request, slug):
    carrito = request.session.get('carrito', {})
    if slug in carrito:
        del carrito[slug]
        request.session['carrito'] = carrito
    return redirect('carrito:ver')

# Vista de pedidos del usuario
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
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from carrito.models import Pedido, ItemPedido
from pages.models import Vino
from django.contrib.auth.models import User
from messenger.models import Message  # ✅ modelo correcto

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

        # ✅ Mensaje interno con resumen sensorial
        sistema = User.objects.filter(username="sistema").first() or request.user

        Message.objects.create(
            sender=sistema,
            recipient=request.user,
            subject="🧾 Confirmación de pedido",
            body=f"""
Hola {request.user.first_name or request.user.username},

Tu pedido #{pedido.id} fue confirmado con éxito el {pedido.creado_en.strftime('%d/%m/%Y %H:%M')}.
Total: ${pedido.total:.2f}

Detalle del pedido:
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