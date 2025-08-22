from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'avatar_preview')
    search_fields = ('user__username', 'bio')

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" style="max-height: 60px; border-radius: 4px;" />', obj.avatar.url)
        return "—"
    avatar_preview.short_description = "Avatar"