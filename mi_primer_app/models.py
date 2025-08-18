from django.db import models

class Vino(models.Model):
    TIPO_CHOICES = [
        ('Tinto', 'Tinto'),
        ('Blanco', 'Blanco'),
        ('Rosado', 'Rosado'),
        ('Espumante', 'Espumante'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    año = models.PositiveIntegerField()
    origen = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='vinos/', blank=True, null=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} ({self.año})"

