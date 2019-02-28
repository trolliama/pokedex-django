from django.test import TestCase
from .functions.coletor_categoria import collect as collectCat
from .functions.coletor_tipos_habilidades import collect as collectTH
from .functions.Pokemon.collectPoke import connect
from .functions.downloadImages import connect as conImgs
from pokedex.models import *

# Create your tests here.
class ColetorCategoriaTeste(TestCase):
    def setUp(self):
        collectCat()

    def test_scrapy(self):
        self.assertNotEqual(len(Categoria.objects.all()), 1)


class ColetorTiposHabilidadesTest(TestCase):

    def setUp(self):
        collectTH()

    def test_scrapy(self):
        self.assertEqual(len(Tipos.objects.all()), 18)
        self.assertEqual(len(Habilidades.objects.all()), 233)


class ColetorPokemonTest(TestCase):

    def setUp(self):
        collectTH()
        collectCat()
        Sexos.objects.create(sexo="?")
        Sexos.objects.create(sexo="M")
        Sexos.objects.create(sexo="F")
        connect()

    def test1(self):
        # Pokemons.objects.get(i)
        # print(
        #     p.nome,
        #     p.vida,
        #     p.ataque,
        #     p.defesa,
        #     p.ataqueSp,
        #     p.defesaSp,
        #     p.velocidade,
        #     p.descricao,
        #     p.altura,
        #     p.peso,
        #     p.categoria,
        #     p.id_evolucao,
        #     p.tipos.all(),
        #     p.fraquezas.all(),
        #     p.sexo.all(),
        #     p.habilidades.all()
        # )
        self.assertEqual(Pokemons.objects.all())


class DownloadImagesTest(TestCase):

    def test1(self):
        conImgs()
