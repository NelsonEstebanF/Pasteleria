from django.shortcuts import render
from .models import Postre

def home(request):
    prostrecitos = Postre().objects.all()
    return render(request, 'core/index.html', {'postres': prostrecitos})