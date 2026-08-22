from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationTestCase(APITestCase):
    def setUp(self):
        self.username = User.objects.create_superuser(username='admin', password='admin')
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.url = reverse('Estudantes-list')

    def test_authenticacao_user_com_credenciais_corretas(self):
        """Teste que verifica a autenticação do usuário"""
        user = authenticate(username=self.username, password=self.password)
        self.assertIsNotNone(user)
        self.assertEqual(user.username, self.username)

    def test_authenticate_invalid_user(self):
        """Teste que verifica a autenticação com credenciais inválidas"""
        user = authenticate(username='invaliduser', password='invalidpassword')
        self.assertIsNone(user)

    def test_authenticate_invalid_password(self):
        """Teste que verifica a autenticação com senha inválida"""
        user = authenticate(username='admin', password='invalidpassword')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_requisicao_get_autorizada(self):
        """Teste que verifica se uma requisição GET é autorizada para um usuário autenticado"""
        self.client.force_authenticate(self.usuario) 
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)