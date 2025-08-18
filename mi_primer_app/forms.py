from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Vino  # eliminá Bodega y Reseña si no existen

# 🍷 Formulario para Bodega
class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = '__all__'

# 🍇 Formulario para Vino
class VinoForm(forms.ModelForm):
    class Meta:
        model = Vino
        fields = '__all__'

# 📝 Formulario para Reseña
class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = '__all__'
