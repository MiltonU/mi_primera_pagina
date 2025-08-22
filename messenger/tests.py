from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Message

User = get_user_model()

class MessengerFlowTest(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username="milton", password="1234")
        self.recipient = User.objects.create_user(username="lucia", password="1234")
        self.client.login(username="milton", password="1234")

    def test_compose_message(self):
        response = self.client.post(reverse("messenger:compose"), {
            "recipient": self.recipient.id,
            "subject": "Prueba sensorial",
            "body": "Este es un mensaje con atmósfera boutique.",
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Message.objects.count(), 1)

    def test_inbox_view(self):
        Message.objects.create(sender=self.sender, recipient=self.recipient, subject="Hola", body="¿Cómo estás?")
        self.client.logout()
        self.client.login(username="lucia", password="1234")
        response = self.client.get(reverse("messenger:inbox"))
        self.assertContains(response, "Hola")

    def test_reply_flow(self):
        original = Message.objects.create(sender=self.sender, recipient=self.recipient, subject="Consulta", body="¿Tenés tiempo?")
        self.client.logout()
        self.client.login(username="lucia", password="1234")
        response = self.client.post(reverse("messenger:reply", args=[original.pk]), {
            "subject": "Re: Consulta",
            "body": "Sí, contá conmigo.",
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Message.objects.count(), 2)