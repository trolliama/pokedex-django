from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from pokedex.models import Tipos, Habilidades
from django.db import transaction, IntegrityError

def insert_types(tipo_):
    try:
        with transaction.atomic():
            Tipos(tipo=tipo_).save()
    except IntegrityError:
        return None

def insert_ability(habilidade_):
    try:
        with transaction.atomic():
            Habilidades(habilidade=habilidade_).save()
    except IntegrityError:
        return None

def collect():
    URLS = {'https://pokemondb.net/ability': insert_ability, 'https://pokemondb.net/type': insert_types}
    
    for url in URLS.keys():
        reqs = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html_code = BeautifulSoup(urlopen(reqs).read(), 'html.parser').find('tbody')

        for link_data in html_code.find_all('a'):
            URLS[url](str(link_data.string))
