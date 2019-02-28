from .ScrapyPokesClass import Pokemon
from urllib.request import urlopen,Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def connect():
    try:
        print('Tentando conexão...')
        req = Request('https://pokemondb.net/pokedex/all', headers={'User-Agent': 'Mozilla/5.0'})
        html = BeautifulSoup(urlopen(req).read(), 'html.parser').find('tbody')

        print('Conexão feita com sucesso!\nIniciando coleta de dados...')

    except HTTPError as e:
        print('Falha na conexão: ', e)

    else:
        get_pokes(html)

def get_pokes(html):
    # poke_id_initial na verdade é o ultimo pokémon a ser cadastrado
    # já que é preciso cadastrar os pokémons de trás para frente para
    # que não haja problemas ao cadastrar suas evoluções
    tags_list = html.find_all('tr', recursive=False)

    for tr in tags_list: # Foi colocado um limite pois o segundo site em que é usado para extrair informações não tem o último pokémon do primeiro site
        if tr.td.find_next_sibling("td").small:
            continue
        poke_id = tr.td['data-sort-value']
        poke = Pokemon(poke_id)

        url_2 = poke.collect_data_tbpokemons(tr)
        poke.collect_idevolucao(url_2)
        poke()
        poke.collectTypes(url_2)
        poke.collectWeaknesses(url_2)
