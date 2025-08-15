from django.shortcuts import render, redirect

# Vista principal
def home(request):
    return render(request, 'mi_primer_app/home.html')

# Vista de login
def login_view(request):
    return render(request, 'mi_primer_app/login.html')

# Vista de registro
def registro_view(request):
    return render(request, 'mi_primer_app/registro.html')
