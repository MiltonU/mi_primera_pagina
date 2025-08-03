from django.db import models

class Bodega(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la bodega")
    pais = models.CharField(max_length=50, verbose_name="País de origen")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")

    def __str__(self):
        return self.nombre

class Vino(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del vino")
    tipo = models.CharField(max_length=50, verbose_name="Tipo (Malbec, Cabernet...)")
    año = models.PositiveIntegerField(verbose_name="Año de cosecha")
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, related_name="vinos")

    def __str__(self):
        return f"{self.nombre} ({self.año})"

class Reseña(models.Model):
    vino = models.ForeignKey(Vino, on_delete=models.CASCADE, related_name="reseñas")
    usuario = models.CharField(max_length=100, verbose_name="Usuario")
    texto = models.TextField(verbose_name="Comentario")
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Reseña de {self.usuario} para {self.vino.nombre}"
