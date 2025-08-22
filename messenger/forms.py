from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["recipient", "subject", "body"]
        widgets = {
            "recipient": forms.Select(attrs={
                "class": "form-select",
            }),
            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Título editorial del mensaje",
            }),
            "body": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 6,
                "placeholder": "Escribí con narrativa sensorial...",
            }),
        }
        labels = {
            "recipient": "Para",
            "subject": "Asunto",
            "body": "Mensaje",
        }