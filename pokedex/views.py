from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Pokemons
# Create your views here.
class IndexView(ListView):
    model = Pokemons
    context_object_name = 'pokemons'
    queryset = Pokemons.objects.all()
    template_name = 'pokedex/index.html'
