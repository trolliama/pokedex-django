from django.urls import path

from .views import *

app_name = "scrapy"
urlpatterns = [
    path('', scrapy_view, name="index"),
    path('scrapy-tipos', scrapy_tipos_view, name="tipos"),
    path('scrapy-habilidades', scrapy_habilidades_view, name="habilidades"),
    path('scrapy-categorias', scrapy_categorias_view, name="categorias"),
    path('scrapy-pokemons', scrapy_pokemons_view, name="pokemons"),
]
