from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login

def hola_mundo(request):
    return HttpResponse('¡Hola, mundo!')

def home(request):
    if request.method == 'POST':
        if request.POST.get('mayor') == 'sí':
            return redirect('mostrar_login')  # Asegurate que esté definido en tus urls
        else:
            return render(request, 'acceso_denegado.html')
    return render(request,'mi_primer_app/home.html')


def mostrar_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            clave = form.cleaned_data['password']
            user = authenticate(request, username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return redirect('home')  # O la vista que quieras
            else:
                form.add_error(None, 'Credenciales inválidas')
    else:
        form = LoginForm()

    return render(request, 'mi_primer_app/login.html', {'form': form})

