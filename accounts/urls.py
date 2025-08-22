from django.urls import path
from .views import InboxView

urlpatterns = [
    path('', InboxView.as_view(), name='inbox'),
]