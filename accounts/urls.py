from django.urls import path
from . import views

app_name = 'messenger'

urlpatterns = [
    path('', views.InboxView.as_view(), name='inbox'),
    path('sent/', views.SentView.as_view(), name='sent'),
    path('new/', views.MessageCreateView.as_view(), name='compose'),
    path('<int:pk>/', views.MessageDetailView.as_view(), name='detail'),
]