from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    descripcion_sensorial = models.TextField(blank=True)
    region = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"