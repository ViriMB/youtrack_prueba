   
from api.models import Persona
from rest_framework import serializers


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['nombre', 'edad', 'sexo']