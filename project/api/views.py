from django.shortcuts import render
from rest_framework.decorators import api_view
from api.models import Persona
from api.serializers import PersonaSerializer
from rest_framework.response import Response
from rest_framework import serializers, status

# Create your views here.
@api_view(['GET'])
def get_personas(request):
        try:
            personas= Persona.objects.all()
            serializers_personas= PersonaSerializer(personas, many=True)
            return Response(serializers_personas.data)           
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)