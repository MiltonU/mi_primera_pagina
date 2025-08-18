from django.db import models

class Bodega(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Vino(models.Model):
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    reseña = models.TextField()

    def __str__(self):
        return f"{self.nombre} ({self.bodega.nombre})"
