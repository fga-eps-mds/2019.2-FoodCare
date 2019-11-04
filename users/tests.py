from django.test import TestCase
from users.models import Usuario
from django.contrib.auth.models import User


# Create your tests here.
class TesteUsuario(TestCase):
    def testa_usuario(self):
        User.objects.create_user(
                username="pedro",
                first_name="Pedrao",
                last_name="Alves",
                password="123"
                )

        usuario = Usuario.objects.filter(user__username="pedro")[0]
        usuario.cnpj = "123456789"
        usuario.save()

        self.assertEqual(str(usuario), "123456789 pedro Pedrao Alves")
