from django.db import models
from django.contrib.auth.models import User
from pages.models import Vino  # Asegurate de que Vino esté en pages.models

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Cliente")
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total del pedido")

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ["-creado_en"]

    def __str__(self):
        return f"Pedido #{self.id} — {self.usuario.username}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Vino, on_delete=models.CASCADE, verbose_name="Vino")
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio unitario")

    class Meta:
        verbose_name = "Item de Pedido"
        verbose_name_plural = "Items de Pedido"

    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"{self.cantidad} × {self.producto.nombre} — Pedido #{self.pedido.id}"