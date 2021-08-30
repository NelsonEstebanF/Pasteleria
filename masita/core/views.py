from django.shortcuts import render
from .models import Project

# Create your views here.
def index(request):
    todos_los_proyectos =  Project.objects.all()
    return render(request, 'core/index.html', {'projects': todos_los_proyectos})
    