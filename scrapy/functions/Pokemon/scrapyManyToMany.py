from pokedex.models import (
    Pokemons,
    Sexos,
    Habilidades,
    Tipos
)

class ScrapyMTM():

    def collectSexo(self, div):
        icons = list(map(lambda x: x['class'][1], div.find_all('i'))) # vai retirar apenas os valores das classes, o retorno é um split() do valor, por isso uso o índice '1'

        if not icons:
            sexo = ['?']
        elif len(icons) > 1:
            sexo = ['M', 'F']
        else:
            sexo = ['M'] if icons[0] == 'icon_male_symbol' else ['F']

        for s in sexo:
            self.poke.sexo.add(Sexos.objects.get(sexo=s))


    def collectAbilitys(self, li):
        for span in li.find_all('span', class_='attribute-value'):
            habilidade_ = str(span.string)
            self.poke.habilidades.add(Habilidades.objects.get(habilidade=habilidade_))

    def collectTypes(self, url):
        div = url.find('div', class_='dtm-type')

        for tag in div.find_all('a'):
            tipo_ = str(tag.string)
            self.poke.tipos.add(Tipos.objects.get(tipo=tipo_))


    def collectWeaknesses(self, url):
        div = url.find('div', class_='dtm-weaknesses')
        weaks = []

        for link in div.find_all('a'):
            weak = link['href'] # Retira o link da tag
            ind = weak.find('=') + 1 # Procura pela substring e adiciona mais um para começar a partir da primeira letra do tipo

            fraqueza_ = str(weak[ind: ].capitalize())
            self.poke.fraquezas.add(Tipos.objects.get(tipo=fraqueza_))
