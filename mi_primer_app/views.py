from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import VinoForm
from .models import Vino, Bodega  # ✅ Import limpio y funcional

# Decorador boutique: edad verificada + login
def acceso_boutique(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('edad_verificada'):
            return redirect('verificar_edad')
        if not request.user.is_authenticated:
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper

# Verificación de edad
def verificar_edad(request):
    if request.method == 'POST':
        respuesta = request.POST.get('respuesta')
        if respuesta == 'si':
            request.session['edad_verificada'] = True  # ✅ Guardar verificación
            return redirect('login')
        else:
            return render(request, 'mi_primer_app/acceso_denegado.html')
    return render(request, 'mi_primer_app/verificar_edad.html')

# Registro de usuario nuevo
def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('buscar_vino')
    else:
        form = UserCreationForm()
    return render(request, 'mi_primer_app/registro.html', {'form': form})

# Login personalizado con verificación de edad
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # ✅ Estética boutique

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('edad_verificada'):
            return redirect('verificar_edad')
        return super().dispatch(request, *args, **kwargs)

# Logout explícito
def cerrar_sesion(request):
    logout(request)
    return redirect('login')

# Buscar vino con filtros refinados
@acceso_boutique
def buscar_vino(request):
    vinos = Vino.objects.all()
    bodegas = Bodega.objects.all()

    # Filtros refinados
    cepa = request.GET.get('cepa')
    terroir = request.GET.get('terroir')
    bodega_id = request.GET.get('bodega')
    pais = request.GET.get('pais')
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')

    if cepa:
        vinos = vinos.filter(cepa__icontains=cepa)
    if terroir:
        vinos = vinos.filter(terroir__icontains=terroir)
    if bodega_id:
        vinos = vinos.filter(bodega__id=bodega_id)
    if pais:
        vinos = vinos.filter(bodega__pais__icontains=pais)
    if precio_min:
        vinos = vinos.filter(precio__gte=precio_min)
    if precio_max:
        vinos = vinos.filter(precio__lte=precio_max)

    return render(request, 'mi_primer_app/buscar.html', {
        'vinos': vinos,
        'bodegas': bodegas
    })

# Agregar vino
@acceso_boutique
def agregar_vino(request):
    if request.method == 'POST':
        form = VinoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('agregar_vino')
    else:
        form = VinoForm()
    return render(request, 'mi_primer_app/formulario.html', {'form': form})

# Comprar vino (pendiente: implementación boutique)
@acceso_boutique
def comprar_vino(request, vino_id):
    vino = get_object_or_404(Vino, id=vino_id)
    # Lógica de compra pendiente: carrito, confirmación, etc.
    return render(request, 'mi_primer_app/compra_confirmada.html', {'vino': vino})
