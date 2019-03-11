from .ScrapyPokesClass import Pokemon
from urllib.request import urlopen,Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def verify_small_and_next_id_poke(current_id_poke, tr_current, tr_next):
    """Verfifica se tem a tag small e se o próximo pokémon
    tem o mesmo id do atual. Se não tiver o mesmo id não podemos pular."""
    has_small = bool(tr_current.td.find_next_sibling("td").small)
    id_next_poke = int(tr_next.td['data-sort-value'])
    has_same_id = id_next_poke == current_id_poke

    if has_small and has_same_id:
        return False
    return True

def connect(initial_id):
    try:
        print('Tentando conexão...')
        req = Request('https://pokemondb.net/pokedex/all', headers={'User-Agent': 'Mozilla/5.0'})
        html = BeautifulSoup(urlopen(req).read(), 'html.parser').find('tbody')

        print('Conexão feita com sucesso!\nIniciando coleta de dados...')

    except HTTPError as e:
        print('Falha na conexão: ', e)

    else:
        get_pokes(html, initial_id)

def get_pokes(html, initial_id):
    # poke_id_initial na verdade é o ultimo pokémon a ser cadastrado
    # já que é preciso cadastrar os pokémons de trás para frente para
    # que não haja problemas ao cadastrar suas evoluções
    tags_list = html.find_all('tr', recursive=False)[::-1]
    count = 0
    while count <= len(tags_list) - 1:
        tr = tags_list[count]

        poke_id = int(tr.td['data-sort-value'])

        if initial_id >= poke_id:
            verified = True if count == len(tags_list) - 1 else verify_small_and_next_id_poke(poke_id, tr, tags_list[count + 1])
            if not verified:
                count += 1
                continue

            poke = Pokemon(poke_id)
            url_2 = poke.collect_data_tbpokemons(tr)
            poke.collect_idevolucao(url_2)
            poke()
            poke.collectTypes(url_2)
            poke.collectWeaknesses(url_2)

        count += 1
