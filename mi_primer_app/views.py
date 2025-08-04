from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm, BodegaForm, VinoForm, ReseñaForm
from .models import Vino

# 🧪 Vista de prueba
def hola_mundo(request):
    return HttpResponse('¡Hola, mundo!')

# 🏡 Página de inicio con verificación de edad
def home(request):
    if request.method == 'POST':
        if request.POST.get('respuesta') == 'si':
            request.session['verificado'] = True
            return redirect('mostrar_login')
        else:
            return redirect('rechazo')
    return render(request, 'mi_primer_app/home.html')


# ❌ Vista para usuarios que no son mayores de edad
def rechazo(request):
    return render(request, 'mi_primer_app/acceso_denegado.html')

# 🔐 Vista de login con formulario personalizado
def mostrar_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            clave = form.cleaned_data['password']
            user = authenticate(request, username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Credenciales inválidas')
    else:
        form = LoginForm()

    return render(request, 'mi_primer_app/login.html', {'form': form})

# 📝 Registro de nuevo usuario
def registro_usuario(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        nuevo_usuario = User.objects.create_user(
            username=usuario,
            email=email,
            password=password
        )
        login(request, nuevo_usuario)
        return redirect('home')
    return render(request, 'mi_primer_app/registro.html')

# 📥 Vista para ingresar datos a 3 modelos
@login_required
def crear_objetos(request):
    if request.method == 'POST':
        bodega_form = BodegaForm(request.POST)
        vino_form = VinoForm(request.POST)
        reseña_form = ReseñaForm(request.POST)

        if bodega_form.is_valid() and vino_form.is_valid() and reseña_form.is_valid():
            bodega = bodega_form.save()
            vino = vino_form.save(commit=False)
            vino.bodega = bodega
            vino.save()

            reseña = reseña_form.save(commit=False)
            reseña.vino = vino
            reseña.save()

            return redirect('home')
    else:
        bodega_form = BodegaForm()
        vino_form = VinoForm()
        reseña_form = ReseñaForm()

    return render(request, 'mi_primer_app/formulario.html', {
        'bodega_form': bodega_form,
        'vino_form': vino_form,
        'reseña_form': reseña_form
    })

# 🔍 Búsqueda por nombre de vino
@login_required
def buscar_vinos(request):
    resultados = []
    query = request.GET.get('query', '')
    if query:
        resultados = Vino.objects.filter(nombre__icontains=query)

    return render(request, 'mi_primer_app/busqueda.html', {
        'resultados': resultados,
        'query': query
    })

def verificar_edad(request):
    if request.method == "POST":
        respuesta = request.POST.get("respuesta")
        if respuesta == "si":
            request.session['mayor_edad'] = True
            return redirect('home')
        else:
            return redirect('login')  # o podés mostrar un mensaje de salida
    return render(request, 'mi_primer_app/verificacion_edad.html')
