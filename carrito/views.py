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
