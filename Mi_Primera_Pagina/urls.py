from django.contrib import admin
from django.urls import path, include
from Mi_Primera_Pagina.views import home_view, about_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 🌿 Página principal y narrativa sensorial
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),

    # 🍷 App de vinos (listado, detalle, filtros)
    path('pages/', include(('pages.urls', 'pages'), namespace='pages')),

    # 👤 Autenticación y perfiles (sin duplicar "accounts/")
    path('accounts/', include('accounts.urls')),

    # 💬 Mensajería interna
    path('messenger/', include(('messenger.urls', 'messenger'), namespace='messenger')),

    # 🔐 Administración
    path('admin/', admin.site.urls),

    # 🔐 Recuperación de contraseña (mantener dentro de "accounts/")
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # 🛒 Carrito de compras
    path('carrito/', include('carrito.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)