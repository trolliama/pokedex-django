from urllib.request import urlopen,Request, urlretrieve
from bs4 import BeautifulSoup
from .Pokemon.GenerateUrl import GenerateUrl

DIRNAME = 'pokedex/static/pokedex/images'

def download_image(url, id):
    """Função para o download das imagens do pokemon.
    Especifique a partir de qual pokémon você deseja baixar as imagens
    informando seu id.
    """
    for tr in url.find_all('tr'):
        td = tr.find('td', class_='cell-num cell-fixed')  #  Alguns pokémons com a tag 'small' na primeira tag 'td'

        if td['data-sort-value'] != str(id) or td.find_next_sibling('td').small:       #  são pokémons que ja passaram, no entanto com um estilo diferente,
            continue                               #  estes não nos interessam e por isso é verificado se o ip ja foi repetido.

        td = tr.find('td',class_='cell-name')
        poke_name = td.string

        url = GenerateUrl(poke_name).generate()
        div_imagem = url.find('div', class_='profile-images')
        link_imagem = div_imagem.find('img')['src']

        pathArq = DIRNAME + '/' + str(id) + '.png'

        urlretrieve(link_imagem, pathArq)
        id += 1  # Adiciona mais um para o id do próximo pokémon

        print('Imagem do %s foi baixada' % poke_name)


def connect():
    try:
        req = Request('https://pokemondb.net/pokedex/all', headers={'User-Agent': 'Mozilla/5.0'})
        url_cod = BeautifulSoup(urlopen(req).read(), 'html.parser').find('tbody')
    except Exception as e:
        print('Conexão falhada: ', e)

    else:
        print('conexão feita com sucesso!')
        download_image(url_cod, int(input("Qual id do pokémon inicial? ")))
