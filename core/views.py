from django.shortcuts import render
from .models import Postre

def masita(request):
    prostrecitos = Postre().objects.all()
    return render(request, 'core/masita.html', {'postres': prostrecitos})