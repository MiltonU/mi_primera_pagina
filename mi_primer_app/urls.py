from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),               # raíz
    path('login/', views.mostrar_login, name='mostrar_login'),
]
