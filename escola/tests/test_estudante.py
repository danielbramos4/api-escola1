from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class EstudantesTestCase(APITestCase):
    def setUp(self):
        self.username = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.username)
        self.estudante_01 = Estudante.objects.create(
            nome='Estudante um', 
            email='teste@email.com', 
            cpf='12345678901',
            data_nascimento='2000-01-01',
            celular = '99 9999-9999'
        )
        self.estudante_02 = Estudante.objects.create(
            nome='Estudante dois', 
            email='teste2@email.com', 
            cpf='12345678902',
            data_nascimento='2000-01-01',
            celular = '99 9999-9999'
        )

    def test_requisicao_get_para_listar_estudantes(self):
        """Teste de requisição GET para listar estudantes"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_um_estudante(self):
        """Teste de requisição GET para listar um estudante"""
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serializados = EstudanteSerializer(instance=dados_estudante).data
        self.assertEqual(response.data, dados_estudante_serializados)

    def test_requisicao_post_para_criar_estudante(self):
        """Teste de requisição POST para criar um estudante"""
        dados = {
            'nome': 'Estudante três',
            'email': 'tete@gmail.com',
            'cpf': '12345678903',
            'data_nascimento': '2000-01-01',
            'celular': '99 9999-9999'
        }
        response = self.client.post(self.url,dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_um_estudante(self):
        """Teste de requisição DELETE para deletar um estudante"""
        response = self.client.delete(self.url+'2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_requsicao_put_para_atualizar_um_estudante(self):
        """Teste de requisição PUT para atualizar um estudante"""
        dados = {
            'nome': 'Teste',
            'email': 'testeput@email.com',
            'cpf': '12345678905',
            'data_nascimento': '2000-01-01',
            'celular': '99 9999-9999'
        }
        response = self.client.put(self.url+'1/', dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)