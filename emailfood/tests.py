from django.test import TestCase, Client
from .views import mensagem, index, email
from django.conf import settings
from django.core.mail import send_mail


class TestaEmail(TestCase):
    def testa_mensagem(self):
        msg_teste = mensagem(
            'Hugo Aragao',
            'hugo@gmail.com',
            'Teste de mensagem'
        )

        msg_gabarito = "\n\nNome: Hugo Aragao\nMensagem: Teste de mensagem\nEmail: hugo@gmail.com\n"

        self.assertEqual(msg_teste, msg_gabarito)
    
    def testa_request_email(self):
         client = Client()
         response = client.post('email/',{'nome':'Fulano','email':'fulano@gmail.com','msg':'Hello email teste'})
         code_expected =404
         self.assertEqual(code_expected,response.status_code)
