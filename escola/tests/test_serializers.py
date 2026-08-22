from django.test import TestCase
from escola.models import Estudante
from escola.serializers import EstudanteSerializer

class SerializerEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante(
            nome= "Teste de Serializer",
            cpf = '98765432100',
            data_nascimento='1995-05-15',
            email='teste.serializer@example.com',
            celular='83 98888-8888'
        )
        self.serializer = EstudanteSerializer(instance=self.estudante)

    def test_verifica_campos_do_serializer(self):
        """Teste que verifica os campos do serializer de Estudante"""
        dados = self.serializer.data
        self.assertEqual(set(dados.keys()), set(['id', 'nome', 'cpf', 'data_nascimento', 'email', 'celular']))
    def test_verifica_conteudo_dos_campos_serializados_de_estudante(self):
        """Teste que verifica o conteúdo dos campos do serializer de Estudante"""
        dados = self.serializer_estudante.data
        self.assertEqual(dados['nome'],self.estudante.nome)
        self.assertEqual(dados['cpf'],self.estudante.cpf)
        self.assertEqual(dados['data_nascimento'],self.estudante.data_nascimento)
        self.assertEqual(dados['email'],self.estudante.email)
        self.assertEqual(dados['celular'],self.estudante.celular)
        
