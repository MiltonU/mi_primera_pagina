from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout

def home_view(request):
    # 🧼 Limpiar sesión al llegar
    request.session.pop('mayor_edad', None)

    # 🧠 Si ya validó edad, redirigir al listado sensorial
    if request.session.get('mayor_edad'):
        return redirect(reverse('pages:vino_list'))
    
    if request.user.is_authenticated:
        logout(request)  # Cierra la sesión al cargar el home
        return render(request, 'home.html')



    # 🎯 Procesar respuesta del formulario
    if request.method == 'POST':
        respuesta = request.POST.get('respuesta')
        if respuesta == 'si':
            request.session['mayor_edad'] = True
            return redirect(reverse('accounts:login'))  # 🔁 Redirige al login boutique
        else:
            return render(request, 'denegado.html')     # 🚫 Vista sensorial de acceso denegado

    # 🏠 Renderizar home con atmósfera editorial
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')