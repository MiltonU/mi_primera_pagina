from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    # Redirección inicial
    path('', lambda request: redirect('verificar_edad'), name='root_redirect'),

    # Admin
    path('admin/', admin.site.urls),

    # Autenticación
    path('accounts/', include('django.contrib.auth.urls')),

    # App principal
    path('inicio/', include('mi_primer_app.urls')), 
   
    path('pages/', include('pages.urls')),
]