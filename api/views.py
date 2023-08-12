from rest_framework.decorators import api_view, renderer_classes, parser_classes, action,\
    authentication_classes, permission_classes
# Classes de rendu JSON, XML, Form
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer, MultiPartRenderer
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
from app_one.models import Student, Note
from .serializers import StudentSerializer, NoteSerializer
from rest_framework import filters, pagination, status
from django.shortcuts import get_object_or_404

# Vue basée sur une fonction
@api_view(['GET', 'POST'])
# Définition des classes d'analyse dans une vue basée sur une fonction
@parser_classes([MultiPartParser])
@renderer_classes([JSONRenderer, XMLRenderer, MultiPartRenderer, TemplateHTMLRenderer])
def hello_world(request):
    image = request.FILES.get('image')
    name = request.data.get('name')
    data = {'message': {'date': '2023-08-05', 'nom': 'test'},
            'images': image,
            'name': name
            }
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
@renderer_classes([JSONRenderer])
@parser_classes([JSONParser, MultiPartParser])
def parse_data(request):
     # Accès aux données via request.data et request.FILES
     # retour des données via Response 
     return Response(request.data)


# Vue basée sur une classe
class TestViewset(viewsets.ViewSet):
    
    def list(self):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    
    def retrieve(self):
        pass
    

class NoteAPIView(APIView):
    
    def get(self, request, id):
        if id:
            try:
                note = Note.objects.get(pk=id)
            except Note.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = NoteSerializer(note)
            return Response(serializer.data)
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        pass
    
    def put(self, request):
        pass
    
    def delete(self, request):
        pass


class ClasseFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        classe = request.query_params.get('classe')

        if classe:
            queryset = queryset.filter(classe__exact=classe)

        return queryset


class MyPagination(pagination.PageNumberPagination):
    page_size = 2  # Set the default page size
    page_size_query_param = 'page_size'

# Vue basée sur une classe (ModelViewSet)
class StudentModelViewset(viewsets.ModelViewSet):
    # Définition des classes d'analyse dans une classe
    parser_classes = [MultiPartParser, JSONParser]
    # Définition des classes de rendu dans une classe
    # renderer_classes = [JSONRenderer, XMLRenderer]
    # Définition du serializer
    serializer_class = StudentSerializer
    # Définition de la queryset qui contient tous les éléments d'une table
    queryset = Student.objects.all()
    # serlializer_class = StudentSerializer
    # filter_backends = [ClasseFilter]
    # pagination_class = MyPagination
    # page_size = 3
    
    @action(detail=False, url_path='recent-students')
    def recent_users(self, request):
        recent_students = Student.objects.all().order_by('age')
        serializer = self.get_serializer(recent_students, many=True)
        return Response(serializer.data)
    
class ClasseFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        classe = request.query_params.get('classe')

        if classe:
            queryset = queryset.filter(classe__exact=classe)

        return queryset