from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from .functions.coletor_categoria import collect as collectCat
from .functions.coletor_tipos_habilidades import  collect_types, collect_ability
from .functions.Pokemon.collectPoke import connect
from .functions.downloadImages import connect as conImgs
from pokedex.models import *

# Create your tests here

class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_scrapy_tipos(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/scrapy/'))
        self.selenium.find_element_by_id('collapseTipos').click()

        print(len(Tipos.objects.all()))

    def test_scrapy_habilidades(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/scrapy/'))
        self.selenium.find_element_by_id('collapseHabilidades').click()

        print(len(Habilidades.objects.all()))

    def test_scrapy_categorias(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/scrapy/'))
        self.selenium.find_element_by_id('collapseCategorias').click()

        print(len(Categoria.objects.all()))

    def test_scrapy_pokemons(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/scrapy/'))
        self.selenium.find_element_by_id('collapsePokémons').click()

        print(len(Pokemons.objects.all()))


class ColetorCategoriaTeste(TestCase):
    def setUp(self):
        collectCat()

    def test_scrapy(self):
        self.assertNotEqual(len(Categoria.objects.all()), 1)


class ColetorTiposHabilidadesTest(TestCase):

    def setUp(self):
        collect_types()
        collect_ability()

    def test_scrapy(self):
        self.assertEqual(len(Tipos.objects.all()), 18)
        self.assertEqual(len(Habilidades.objects.all()), 233)


class ColetorPokemonTest(TestCase):

    def setUp(self):
        collect_types()
        collect_ability()
        collectCat()
        Sexos.objects.create(sexo="?")
        Sexos.objects.create(sexo="M")
        Sexos.objects.create(sexo="F")
        connect(809)

    def test1(self):
        p = Pokemons.objects.get(id=745)
        print(
            p.nome,
            p.vida,
            p.ataque,
            p.defesa,
            p.ataqueSp,
            p.defesaSp,
            p.velocidade,
            p.descricao,
            p.altura,
            p.peso,
            p.categoria,
            p.poke_evolucao,
            p.tipos.all(),
            p.fraquezas.all(),
            p.sexo.all(),
            p.habilidades.all()
        )


class DownloadImagesTest(TestCase):

    def test1(self):
        conImgs()
