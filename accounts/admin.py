from django.contrib import admin
from django.utils.html import format_html
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date', 'preferencias', 'bio', 'avatar_preview')
    search_fields = ('user__username', 'bio', 'preferencias')
    list_filter = ('birth_date',)
    readonly_fields = ('avatar_preview',)

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html(
                '<img src="{}" style="height:60px; border-radius:50%; object-fit:cover;" />',
                obj.avatar.url
            )
        return "—"
    avatar_preview.short_description = "Avatar"