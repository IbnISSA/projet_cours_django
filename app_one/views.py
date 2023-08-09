from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

# Create your views here.

def index(request):
    # contexte
    data = {
        'responsable': False,
        'nom': 'Almamy', # variable de contexte
        'notes': { # variable de contexte
            'stats': 18,
            'ia': 17,
            'python': 17
        },
        'cours': [ # variable de contexte
            'Django',
            'Mathèmatiques',
            'Bases de données'
        ]
    }
    # syntaxe de passage du contexte au template
    return render(request, 'app_one/index.html', context=data)

def about(request):
    return HttpResponse('Bonjour tout le monde!')

def contact(request, id, name):
    print(id, name)
    return HttpResponse('<h1> Bonjour </h1>')


class AboutView(View):
    
    def get(self, request):
        data = {"note": 15, "matiere": "Maths"}
        return JsonResponse(data)
    
    def post(self, request):
        return HttpResponse("I am not here for now!")
    
    def delete(self, request):
        return HttpResponse("I am not here for now!")