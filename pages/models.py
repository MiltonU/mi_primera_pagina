from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Page(models.Model):
    title = models.CharField("Título", max_length=200, default="Sin título")
    subtitle = models.CharField("Subtítulo", max_length=255, default="Sin subtítulo")
    content = RichTextField("Contenido enriquecido")
    image = models.ImageField("Imagen destacada", upload_to="pages/", blank=True, null=True)
    created_at = models.DateField("Fecha de creación", auto_now_add=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} — {self.subtitle}"