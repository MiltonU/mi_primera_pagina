from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Autenticación (login/logout por defecto)
    path('accounts/', include('django.contrib.auth.urls')),

    # App principal (mi_primera_app)
    path('', include('mi_primera_app.urls')),

    # Otras apps
    path('pages/', include('pages.urls')),
    path('messenger/', include('messenger.urls')),
]