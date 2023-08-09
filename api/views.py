from rest_framework.decorators import api_view, renderer_classes, parser_classes, \
    authentication_classes, permission_classes
# Classes de rendu JSON, XML, Form
from rest_framework.renderers import JSONRenderer, HTMLFormRenderer
from rest_framework_xml.renderers import XMLRenderer
# Classes d'analyse JSON, XML, Form
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework_xml.parsers import XMLParser
# Classes d'authentification
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
# Classes de permissions
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from app_one.models import Student
from .serializers import StudentSerializer
from rest_framework import status

# Vue basée sur une fonction
@api_view(['GET', 'POST'])
# Définition des classes d'analyse dans une vue basée sur une fonction
@renderer_classes([JSONRenderer, XMLRenderer])
def hello_world(request):
    data = {'message': {'date': '2023-08-05', 'nom': 'test'}}
    return Response(data)


@api_view(['GET', 'POST'])
# Définition des classes d'analayse dans une vue basée sur une fonction
@parser_classes([JSONParser, XMLParser])
def parser_func(request):
    data = request.data
    return Response(data)

@api_view(['GET'])
# Définition des classes d'authentification et de permissions
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def token_func(request):
    return Response({'message': 'Authentification réussie !'})

@api_view(['POST'])
@renderer_classes([JSONRenderer, HTMLFormRenderer])
@parser_classes([JSONParser, MultiPartParser])
def parse_data(request):
     # Accès aux données via request.data et request.FILES
     # retour des données via Response 
     return Response(request.data)

# Vue basée sur une classe (ModelViewSet)
class ListStudents(viewsets.ModelViewSet):
    # Définition des classes d'analyse dans une classe
    parser_classes = [MultiPartParser, JSONParser]
    # Définition des classes de rendu dans une classe
    renderer_classes = [JSONRenderer, XMLRenderer]
    # Définition du serializer
    serializer_class = StudentSerializer
    # Définition de la queryset qui contient tous les éléments d'une table
    queryset = Student.objects.all()
    
    # serlializer_class = StudentSerializer
