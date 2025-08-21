from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import VinoForm
from .models import Vino

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
        edad = int(request.POST.get('edad'))
        if edad >= 18:
            request.session['edad_verificada'] = True
            return redirect('login')
        else:
            return render(request, 'mi_primer_app/no_autorizado.html')

    # Si ya verificó edad, va al login
    if request.session.get('edad_verificada'):
        return redirect('login')

    # Muestra el formulario
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

# Vista de login con control de edad
class CustomLoginView(LoginView):
    template_name = 'mi_primer_app/registration/login.html'

    def dispatch(self, request, *args, **kwargs):
        # Si no verificó edad, no puede loguearse
        if not request.session.get('edad_verificada'):
            return redirect('verificar_edad')
        return super().dispatch(request, *args, **kwargs)

# Buscar vino
@acceso_boutique
def buscar_vino(request):
    query = request.GET.get('q')
    resultados = Vino.objects.filter(nombre__icontains=query) if query else Vino.objects.all()
    return render(request, 'mi_primer_app/buscar.html', {'resultados': resultados, 'query': query})

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

# Comprar vino
@acceso_boutique
def comprar_vino(request, vino_id):
    vino = get_object_or_404(Vino, id=vino_id)
    return render(request, 'mi_primer_app/comprar.html', {'vino': vino})

# Redirección inicial
def redireccion_inicio(request):
    return redirect('verificar_edad')


