from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class MatriculasTestCase(APITestCase):
    def setUp(self):
        self.username = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Matriculas-list')
        self.cliente.force_authenticate(user=self.usuario)