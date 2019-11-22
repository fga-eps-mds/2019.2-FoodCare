from django.test import TestCase
from .views import mensagem

class TestaEmail(TestCase):
    def testa_mensagem(self):
        msg_teste = mensagem(
            'Hugo Aragao',
            'hugo@gmail.com',
            'Teste de mensagem'
        )

        msg_gabarito = "\n\nNome: Hugo Aragao\nMensagem: Teste de mensagem\nEmail: hugo@gmail.com\n"

        self.assertEqual(msg_teste, msg_gabarito)
