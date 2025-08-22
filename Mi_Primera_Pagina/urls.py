from django.contrib import admin
from django.urls import path, include

from Mi_Primera_Pagina.views import home_view, about_view

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('pages/', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('messenger/', include('messenger.urls')),
    path('admin/', admin.site.urls),
]