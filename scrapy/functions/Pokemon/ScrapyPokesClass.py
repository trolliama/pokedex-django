from .GenerateUrl import GenerateUrl
from .scrapyManyToMany import ScrapyMTM

from pokedex.models import Categoria, Pokemons

class Pokemon(ScrapyMTM):

    def __init__(self, poke_id):
        self.poke_id = poke_id
        self.data = [poke_id]


    def __call__(self):
        self.poke = Pokemons(*self.data, id=self.poke_id)
        self.poke.save()

        self.collectSexo(self.div_code)
        self.collectAbilitys(self.li_tags[1]) # Aproveita a tag 'li'da função collect_categoria encontrada e chama a função que procura pelas habilidades.


    def collect_desc(self, url):
        """ Coleta a descrição do pokémon"""

        div = url.find('div', class_='version-descriptions active')
        self.data.append(str(div.p.string.strip()))


    def collect_altura_peso(self, url):

        self.div_code = url.find('div', class_='column-7')

        for li in self.div_code.find_all('li', limit=2):
            data = li.find('span', class_='attribute-value')
            value = data.string.split()[0]

            self.data.append(float(value.replace(',', '.')))


    def collect_categoria(self, url):
        self.li_tags = url.find("div", class_="column-7 push-7").find_all('li')

        categoria_ = str(self.li_tags[0].find('span', class_='attribute-value').string)
        id_categoria = Categoria.objects.get(categoria=categoria_).id
        self.data.append(id_categoria)

    def collect_data_tbpokemons(self, tr):
        "Essa func tem como objetivo retirar dados do primeiro e segundo site"

        for td in tr.find_all('td')[1:]:
            classe_valor = td['class'][0]
            if classe_valor not in ('cell-icon', 'cell-total'):  # O atributo da tag 'cell-total' não me interessa
                data = td.a.string if td.small else td.string
                data = str(data) if classe_valor != "cell-num" else int(data)
                self.data.append(data)

        second_url = GenerateUrl(self.data[1]).generate()

        self.collect_desc(second_url)
        self.collect_altura_peso(second_url)
        self.collect_categoria(second_url)

        print('\nDados do pokémon {} - {} coletado com sucesso!!'.format(self.poke_id, self.data[1]))

        return second_url


    def collect_idevolucao(self, url_code):
        div_classe = 'column-12 push-1 dog-ear-bl'
        div_code = url_code.find('div', class_=div_classe)
        li = div_code.find('li', class_='last')
        try:
            id_last = li.find('span').string.strip() # Poderá ser levantada uma exceção caso o pokémon tenha apenas uma versão, pois não existirá uma tag com classe 'last'

            if int(id_last[3: ]) - self.poke_id > 0: # Se o id_last menos o id do pokémon for maior que zero quer dizer que ele tem evolução, se não ser[a levantada uma exceção
                self.data.append(self.poke_id + 1)
                print("Id da evolução do pokémon coletado com sucesso!")
            else: raise ValueError # Levanta a exceção

        except (ValueError, AttributeError) as e:
            self.data.append(None)
            print('Pokémon não tem evolução')
