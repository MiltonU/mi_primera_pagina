from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Bodega, Vino

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = '__all__'

class VinoForm(forms.ModelForm):
    class Meta:
        model = Vino
        fields = ['bodega', 'nombre', 'descripcion']
        labels = {
            'descripcion': 'Reseña',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Notas de cata, maridaje, historia del vino...',
                'class': 'form-control'
            }),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'bodega': forms.Select(attrs={'class': 'form-control'}),
        }

