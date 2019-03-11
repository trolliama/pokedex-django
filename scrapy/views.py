from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .functions import coletor_tipos_habilidades
from .functions.coletor_categoria import collect as collect_cat
from .functions.Pokemon.collectPoke import connect as collect_poke
import time
# Create your views here.

def scrapy_view(request):
    context = {
        "list_items": ["Tipos", "Habilidades", "Categorias", "Pokemons"]
    }
    return render(request, 'scrapy/scrapy_view.html', context)

def scrapy_tipos_view(request):
    print("ue")
    coletor_tipos_habilidades.collect_types()
    return HttpResponseRedirect(reverse('scrapy:index'))

def scrapy_habilidades_view(request):
    print("ue")
    coletor_tipos_habilidades.collect_ability()
    return HttpResponseRedirect(reverse('scrapy:index'))

def scrapy_categorias_view(request):
    print("ue")
    collect_cat()
    return HttpResponseRedirect(reverse('scrapy:index'))

def scrapy_pokemons_view(request):
    try:
        initial_id = int(request.POST['idpoke'])
        if 1 <= initial_id <= 809:
            collect_poke(initial_id)
            pass
        else:
            raise ValueError

    except ValueError as e:
        context = {
            "list_items": ["Tipos", "Habilidades", "Categorias", "Pokemons"],
            "error_message": "Use apenas os números que correspondem ao id de um pokémon existente (1 a 809)"
        }
        return render(request, 'scrapy/scrapy_view.html', context)
    return HttpResponseRedirect(reverse('scrapy:index'))
