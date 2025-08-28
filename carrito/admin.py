from django.contrib import admin
from .models import Pedido, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0
    readonly_fields = ('producto', 'cantidad', 'precio_unitario', 'subtotal')
    can_delete = False

    def subtotal(self, obj):
        return obj.subtotal()
    subtotal.short_description = "Subtotal"

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'creado_en', 'total')
    list_filter = ('creado_en', 'usuario')
    search_fields = ('usuario__username',)
    date_hierarchy = 'creado_en'
    inlines = [ItemPedidoInline]
    readonly_fields = ('usuario', 'creado_en', 'total')

admin.site.register(Pedido, PedidoAdmin)