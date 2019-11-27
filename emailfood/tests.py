from django.test import TestCase
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
    
    def testa_index(self):
        teste_mail = send_mail("FoodCare: Hugo Aragao",
        "\n\nNome: Hugo Aragao\nMensagem: Teste de mensagem\nEmail: hugo@gmail.com\n",
        "foodcare.unb@gmail.com",
        ['teste@gmail.com'],
        fail_silently = False)

        self.assertEquals(teste_mail, 1)
          

