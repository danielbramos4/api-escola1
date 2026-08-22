from django.test import TestCase
from escola.models import Estudante

class ModelEstudanteTestCase(TestCase):
    # def test_falha(self):
    #    self.fail('Teste falhou :(')
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome= "Teste de Modelo",
            cpf = '12345678900',
            data_nascimento='2000-01-01',
            email='teste.modelo@example.com',
            celular = '83 99999-9999'
        )
    def test_verifica_atributos_de_estudantes(self):
        """Teste que verifica os atributos do modelos de Estudante"""
        self.assertEqual(self.estudante.nome, "Teste de Modelo")
        self.assertEqual(self.estudante.cpf, '12345678900')
        self.assertEqual(self.estudante.data_nascimento, '2000-01-01')
        self.assertEqual(self.estudante.email, 'teste.modelo@example.com')
        self.assertEqual(self.estudante.celular, '83 99999-9999')