from django.urls import path
from .views import InboxView
from .views import ProfileView

app_name = 'accounts'


urlpatterns = [
    path('', InboxView.as_view(), name='inbox'),
    path('profile/', ProfileView.as_view(), name='profile'),
]