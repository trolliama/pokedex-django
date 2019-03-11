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

def collect_types():
    print('renn')
    site_url = 'https://pokemondb.net/type'

    reqs = Request(site_url, headers={'User-Agent': 'Mozilla/5.0'})
    html_code = BeautifulSoup(urlopen(reqs).read(), 'html.parser').find('tbody')

    for link_data in html_code.find_all('a'):
        insert_types(str(link_data.string))

def collect_ability():
    print('renn')
    site_url = 'https://pokemondb.net/ability'

    reqs = Request(site_url, headers={'User-Agent': 'Mozilla/5.0'})
    html_code = BeautifulSoup(urlopen(reqs).read(), 'html.parser').find('tbody')

    for link_data in html_code.find_all('a'):
        insert_ability(str(link_data.string))
