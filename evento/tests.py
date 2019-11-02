from django.test import TestCase
from .models  import Evento 
from users.models import Usuario
from datetime import datetime, date
import unittest

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