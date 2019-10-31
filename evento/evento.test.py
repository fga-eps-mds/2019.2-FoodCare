from django.test import TestCase
from .models  import Eventos
from users.models import Usuario

class Usuario(TestCase):
    def setup(self):
        Usuario.objects.create(username="Fulano",cnpj="123456789-0000")
    def test_create_user(self):
        fulano = Usuario.objects.get(username="Fulano")
        self.assertEquals(fulano.username,"Fulano")
        self.assertEquals(fulano.cnpj,"123456789-0000")
