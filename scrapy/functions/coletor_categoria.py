from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from pokedex.models import Categoria
from django.db import transaction, IntegrityError


def get_html():
    url = 'https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_category'

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html_code = BeautifulSoup(urlopen(req).read(), 'html.parser').find('table', class_='sortable')

    return html_code

def collect():

    html_code = get_html()

    for tr in html_code.find_all('tr'):
        try:
            tr['style']
        except KeyError:
            td = tr.find_all('td', limit=4)[-1]
            if td.find('span'):
                categoria_ = td.find('span').string

            else:
                categoria_ = td.string.replace('Pokémon', '')

            try:
                with transaction.atomic():
                    Categoria(categoria=categoria_.strip()).save()
            except IntegrityError:
                pass
