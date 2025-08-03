from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Bodega, Vino, Reseña

# 🔐 Formulario de login personalizado
class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

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
