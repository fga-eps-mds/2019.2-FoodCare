from django.test import TestCase
from django.conf import settings
from django.utils.timezone import make_aware
from django.contrib.auth.models import User
from users.models import Usuario
from datetime import datetime, date
from .models  import Evento, Categoria
import unittest

class TesteEvento(TestCase):
    def testa_evento(self):
        User.objects.create_user(
            username="doador",
            first_name="Doador",
            last_name="Teste",
            password="123456"
        )
        usuario = Usuario.objects.filter(user__username="doador")[0]
        usuario.save()

        categoria = Categoria.objects.create(nome="Frutas")
        categoria.save()

        # ajusta tipo de data
        settings.TIME_ZONE
        data_inicio_utc = make_aware(datetime.now())
        data_final_utc = make_aware(datetime.now())

        evento = Evento.objects.create(
            nome="Doação de banana",
            desc="Bananas entregues sem custos",
            latitude=-15.99033,
            longitude=-48.0455655,
            data_inicio=data_inicio_utc,
            data_final=data_final_utc,
            id_doador=usuario,
            id_categoria=categoria
        )

        self.assertEqual(str(evento), "Doação de banana {}".format(usuario.id))

class TesteCategoria(TestCase):
    def testa_categoria(self):
        categoria = Categoria.objects.create(nome="Fruta")
        categoria.save()
        self.assertEqual(str(categoria), "Fruta")
'''
class EventoTest(unittest.TestCase):
    def setUp(self):
        # o id do doador nao ta funcionando corretamente, o restante esta
        doador = Usuario.objects.create(user="Fulano", cnpj="12345678901234")
        id_doador = doador.id

        self.evento = Evento.objects.create(
            nome="Teste",
            id_doador= id_doador,
            data_inicio=datetime.now(),
            data_final=datetime.now(),
            desc="Apenas um teste"
            )

    def test_criacao_evento(self):
        print("Testando criacao de evento")
        self.assertEqual(self.evento.getID(), "Teste")
        print("Criacao de evento testado")


class TestEvento(TestCase):
    def testa_str_do_objeto(self):
        id_doador = Usuario.objects.create(
            username="doador",
            first_name="Nome",
            last_name="Sobrenome",
            password="123",
        )
        self.assertEqual(str(doador), "doador Nome Sobrenome")

        return doador


    cria_evento = Evento.models.create(
        nome="Teste",
        id_doador_id = 1,
        data_inicio="2019-09-09",
        data_final="2019-09-10",
        desc="Apenas um teste"

    )

'''
