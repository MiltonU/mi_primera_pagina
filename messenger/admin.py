from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("subject", "sender", "recipient", "sent_at", "read")
    list_filter = ("read", "sent_at")
    search_fields = ("subject", "body", "sender__username", "recipient__username")
    readonly_fields = ("sent_at",)
    fieldsets = (
        ("Información principal", {
            "fields": ("sender", "recipient", "subject", "body")
        }),
        ("Estado", {
            "fields": ("read", "sent_at"),
            "classes": ("collapse",)
        }),
    )