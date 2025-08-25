from django.shortcuts import render, redirect
from django.urls import reverse

def home_view(request):
    request.session.pop('mayor_edad', None)
    if request.method == 'POST':
        respuesta = request.POST.get('respuesta')
        if respuesta == 'si':
            request.session['mayor_edad'] = True
            return redirect(reverse('pages:vino_list'))
        else:
            return render(request, 'denegado.html')

    if request.session.get('mayor_edad'):
        return redirect(reverse('pages:vino_list'))

    return render(request, 'home.html')


    return render(request, 'home.html', {'error': error})

    if request.session.get('mayor_edad'):
        return redirect(reverse('pages:vino_list'))

    return render(request, 'home.html', {'error': error})

def about_view(request):
    return render(request, 'about.html')
