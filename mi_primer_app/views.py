from django.shortcuts import render, redirect, get_object_or_404
from .forms import VinoForm
from .models import Vino

def agregar_vino(request):
    if request.method == 'POST':
        form = VinoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('agregar_vino')
    else:
        form = VinoForm()
    return render(request, 'formulario.html', {'form': form})

def comprar_vino(request, vino_id):
    vino = get_object_or_404(Vino, id=vino_id)
    return render(request, 'comprar.html', {'vino': vino})

def verificar_edad(request):
    if request.method == 'POST':
        respuesta = request.POST.get('respuesta')
        if respuesta == 'si':
            request.session['edad_verificada'] = True
            return redirect('login')
        else:
            return render(request, 'mi_primer_app/verificar_edad.html', {
                'denegado': True
            })
    return render(request, 'mi_primer_app/verificar_edad.html')

from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    edad_verificada = request.session.get('edad_verificada', False)
    return render(request, 'mi_primer_app/home.html', {
        'edad_verificada': edad_verificada
    })