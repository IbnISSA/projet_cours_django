from django.contrib import admin
from django.urls import path, include
from .views import hello_world, StudentModelViewset, parser_func, token_func, parse_data
from rest_framework.authtoken import views
from rest_framework import routers
from . import views as api_views


# Définition du Routeur qui permet de générer automatiquement des routes pour les vues d'une API REST
router = routers.SimpleRouter()

# Enregistrement de la ressource Student avec sa vue correspondante
router.register(r'students', StudentModelViewset)

urlpatterns = [
    path('rest-api/', hello_world),
    # path('students/', ListStudents.as_view()),
    # path('students/<int:id>/', ListStudents.as_view()),
    path('rest-api-v3/', parser_func),
    path('data-parsing/', parse_data),
    # Le path ci-dessous est soumis à une auhtentication par Token
    path('check-token/', token_func),
    # Le path ci-dessous permet d'obtenir des Tokens en fournissant le username et le password avec une requête POST
    path('api-token-auth/', views.obtain_auth_token),
    path('notes/', api_views.NoteAPIView.as_view()),
    path('notes/<int:id>/', api_views.NoteAPIView.as_view()),
]

# Ajout des urls générées par le routeur dans la liste des urls disponibles dans l'application "api"
urlpatterns += router.urls
