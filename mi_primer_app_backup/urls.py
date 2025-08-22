from django.urls import path
from .views import root_redirect_view, login_view, home_view, buscar_view

urlpatterns = [
    path('', root_redirect_view, name='root_redirect'),
    path('verificar_edad/', verificar_edad_view, name='verificar_edad'),
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('buscar/', buscar_view, name='buscar'),
]
