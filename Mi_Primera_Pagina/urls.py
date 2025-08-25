from django.contrib import admin
from django.urls import path, include
from Mi_Primera_Pagina.views import home_view, about_view

urlpatterns = [
    # 🌿 Página principal y narrativa sensorial
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),

    # 🍷 App de vinos (listado, detalle, filtros)
    path('pages/', include(('pages.urls', 'pages'), namespace='pages')),

    # 👤 Autenticación y perfiles
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),

    # 💬 Mensajería interna
    path('messenger/', include(('messenger.urls', 'messenger'), namespace='messenger')),

    # 🔐 Administración
    path('admin/', admin.site.urls),
]