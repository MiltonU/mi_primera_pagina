from django.shortcuts import render, redirect

def home_view(request):
    if request.method == 'POST':
        edad = request.POST.get('edad')
        if edad and int(edad) >= 18:
            request.session['mayor_edad'] = True
            return redirect('pages:vino_list')  # o 'home' si querés mostrar contenido
        else:
            return render(request, 'home.html', {'error': 'Debés ser mayor de edad para continuar.'})

    if request.session.get('mayor_edad'):
        return redirect('pages:vino_list')  # o mostrar contenido libre

    return render(request, 'home.html')