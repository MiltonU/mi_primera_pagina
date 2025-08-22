from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "author", "created_at")
    list_filter = ("author", "created_at")
    search_fields = ("title", "subtitle", "content")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)

    fieldsets = (
        ("Información principal", {
            "fields": ("title", "subtitle", "author", "created_at")
        }),
        ("Contenido", {
            "fields": ("content", "image")
        }),
    )