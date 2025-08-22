from django.contrib import admin
from .models import Page
from django.utils.html import format_html

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'preview_image')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Ficha académica', {
            'fields': ('title', 'content', 'image')
        }),
        ('Metadatos', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 80px; border-radius: 4px;" />', obj.image.url)
        return "—"
    preview_image.short_description = "Imagen"