from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from .forms import VinoForm
from .models import Vino

def home(request):
    login_form = AuthenticationForm()
    registro_form = UserCreationForm()

    if request.method == 'POST':
        if 'login_submit' in request.POST:
            login_form = AuthenticationForm(data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('home')
        elif 'registro_submit' in request.POST:
            registro_form = UserCreationForm(request.POST)
            if registro_form.is_valid():
                registro_form.save()
                return redirect('login')

    return render(request, 'mi_primer_app/home.html', {
        'login_form': login_form,
        'registro_form': registro_form
    })

def agregar_vino(request):
    if request.method == 'POST':
        form = VinoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect
