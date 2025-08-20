from django.db import models

class Bodega(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255, default="Desconocida")
    pais = models.CharField(max_length=50)
    historia = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='bodegas/', blank=True, null=True)

    def __str__(self):
        return self.nombre


class Vino(models.Model):
    nombre = models.CharField(max_length=100)
    cepa = models.CharField(max_length=50, default="Malbec")
    terroir = models.CharField(max_length=50, default="Mendoza")
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, related_name='vinos')
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    imagen = models.ImageField(upload_to='vinos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.cepa})"

