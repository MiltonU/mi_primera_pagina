from django.shortcuts import render, redirect
from django.urls import reverse

def home_view(request):
    error = None

    if request.method == 'POST':
        edad = request.POST.get('edad')
        try:
            edad = int(edad)
            if edad >= 18:
                request.session['mayor_edad'] = True
                return redirect(reverse('pages:vino_list'))
            else:
                error = 'Debés ser mayor de edad para continuar.'
        except (ValueError, TypeError):
            error = 'Ingresá una edad válida.'

    if request.session.get('mayor_edad'):
        return redirect(reverse('pages:vino_list'))

    return render(request, 'home.html', {'error': error})

def about_view(request):
    return render(request, 'about.html')
