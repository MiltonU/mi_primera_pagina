from django.contrib import admin
from django.urls import path, include
from .views import home_view  # si la vista está en Mi_Primera_Pagina/views.py

urlpatterns = [
    path('', home_view, name='home'),  # ← esta es la raíz del sitio
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('pages/', include('pages.urls')),
    path('messenger/', include('messenger.urls')),

]