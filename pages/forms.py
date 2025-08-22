from django import forms
from .models import Page
from django.forms.widgets import DateInput

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'content', 'image', 'created_at']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título académico con narrativa sensorial'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Contenido enriquecido con atmósfera editorial',
                'rows': 10
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'created_at': DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
        labels = {
            'title': 'Título',
            'content': 'Contenido',
            'image': 'Imagen destacada',
            'created_at': 'Fecha de publicación',
        }