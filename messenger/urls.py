from django.urls import path
from .views import (
    InboxView,
    SentView,
    MessageDetailView,
    ComposeView,
    ReplyView,
    EnviarMensajeView,
    ConversacionView  
)

app_name = "messenger"

urlpatterns = [
    path("inbox/", InboxView.as_view(), name="inbox"),
    path("sent/", SentView.as_view(), name="sent"),
    path("message/<int:pk>/", MessageDetailView.as_view(), name="detail"),
    path("compose/", ComposeView.as_view(), name="compose"),
    path("reply/<int:pk>/", ReplyView.as_view(), name="reply"),
    path("enviar/", EnviarMensajeView.as_view(), name="enviar"),  # ✅ sin user_id
    path("conversacion/<str:username>/", ConversacionView.as_view(), name="conversacion"),
]