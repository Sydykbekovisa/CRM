from django.test import TestCase
from .models import Client


class ClientModelTest(TestCase):
    def test_create_client(self):
        client = Client.objects.create(
            name="Иван Иванов",
            email="ivan@example.com",
            phone_number="+123456789"
        )
        self.assertEqual(client.name, "Иван Иванов")
        self.assertEqual(client.email, "ivan@example.com")
