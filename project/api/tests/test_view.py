import json
from api.serializers import PersonaSerializer
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from api.models import Persona
from api.views import get_personas

cliente = Client()

class GetListPersona(TestCase):

    def setUp(self):
        Persona.objects.create(nombre = 'viri', edad=3, sexo= 'True' )
        Persona.objects.create(nombre = 'viri', edad=3, sexo= 'False' )
        Persona.objects.create(nombre = 'viri', edad=3, sexo= 'False' )
    
    def test_lista_persona(self):
        response = cliente.get('http://127.0.0.1:8000/api/persona/list')
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
