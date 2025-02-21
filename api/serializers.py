from rest_framework import serializers
from app_one.models import Student, Note, User, Event

# Serialiseur permettant de transformer un objet complexe(exemple modèle Django) en un dictionnaire Python
# Ceci est un serialiseur simple
# class StudentSerializer(serializers.Serializer):
#     prenom = serializers.CharField(max_length=100)
#     nom = serializers.CharField(max_length=100)
#     age = serializers.IntegerField()
#     classe = serializers.CharField(max_length=100)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        # fields = ['nom', 'prenom', 'age']

class NoteSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = Note
        fields = "__all__"
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'description', 'start_date', 'end_date')
