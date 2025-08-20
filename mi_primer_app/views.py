from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .forms import VinoForm
from .models import Vino

# Verificación de edad antes del login
def verificar_edad(request):
    if request.method == 'POST':
        respuesta = request.POST.get('respuesta')
        if respuesta == 'si':
            request.session['edad_verificada'] = True
            return redirect('login')
        else:
            return render(request, 'mi_primer_app/verificar_edad.html', {'denegado': True})
    return render(request, 'mi_primer_app/verificar_edad.html')

# Registro de usuario nuevo
def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('formulario')
    else:
        form = UserCreationForm()
    return render(request, 'mi_primer_app/registro.html', {'form': form})

# Vista de login nativo con template personalizado
class CustomLoginView(LoginView):
    template_name = 'mi_primer_app/registration/login.html'

# Formulario para agregar vino (requiere login)
@login_required
def agregar_vino(request):
    if request.method == 'POST':
        form = VinoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('agregar_vino')
    else:
        form = VinoForm()
    return render(request, 'mi_primer_app/formulario.html', {'form': form})

# Vista para comprar vino (requiere login)
@login_required
def comprar_vino(request, vino_id):
    vino = get_object_or_404(Vino, id=vino_id)
    return render(request, 'mi_primer_app/comprar.html', {'vino': vino})

# Vista para buscar vino (requiere login)
@login_required
def buscar_vino(request):
    query = request.GET.get('q')
    resultados = Vino.objects.filter(nombre__icontains=query) if query else []
    return render(request, 'mi_primer_app/buscar.html', {'resultados': resultados, 'query': query})

def home(request):
    return render(request, 'mi_primer_app/home.html')

