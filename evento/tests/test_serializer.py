from django.test import TestCase
from datetime import datetime, date
from evento import serializers
from evento.serializers import *
import unittest

class TesteEventoSerializer(TestCase):
    def setUp(self):
        User.objects.create_user(
                username="lucas",
                first_name="Lucao",
                last_name="lulu",
                password="123"
                )
        usuario = Usuario.objects.filter(user__username="lucas")[0]
        usuario.save()

        self.evento_attributes = {
            'nome': 'arnaldo',
            'id_doador': usuario,
            'data_inicio' : datetime.now(),
            'data_final' : datetime.now(),
            'local' : 'samambaia',
            'desc' : 'lalala'

        }

        self.serializer_data = {
            'nome': 'joao',
            'id_doador': usuario,
            'data_inicio' : datetime.now(),
            'data_final' : datetime.now(),
            'local' : 'taguatinga',
            'desc' : 'lala'
        }

        self.evento = Evento.objects.create(**self.evento_attributes)
        self.serializer = EventoSerializer(instance=self.evento)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(['nome', 'id_doador','data_inicio','data_final','local','desc']))
