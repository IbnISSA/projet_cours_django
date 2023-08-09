from django.db import models

# Create your models here.

class Student(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    age = models.IntegerField()
    classe = models.CharField(max_length=100)
    
    def serialize(self):
        return {
            'prenom': self.prenom,
        }
    

class Note(models.Model):
    matiere = models.CharField(max_length=200)
    note_obtenue = models.FloatField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="notes")


class Professor(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name="professors")
