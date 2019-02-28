from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.categoria


class Tipos(models.Model):
    tipo = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.tipo


class Habilidades(models.Model):
    habilidade = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.habilidade


class Sexos(models.Model):
    sexo = models.CharField(max_length=1, unique=True)

    def __str__(self):
        return self.sexo


class Pokemons(models.Model):
    nome = models.CharField(max_length=15)
    vida = models.IntegerField(default=0)
    ataque = models.IntegerField(default=0)
    defesa = models.IntegerField(default=0)
    ataqueSp = models.IntegerField(default=0)
    defesaSp = models.IntegerField(default=0)
    velocidade = models.IntegerField(default=0)
    descricao = models.CharField(max_length=100, default='')
    altura = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    peso = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=None)
    id_evolucao = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    tipos = models.ManyToManyField(Tipos, related_name='tipos')
    fraquezas = models.ManyToManyField(Tipos, related_name='fraquezas')
    sexo = models.ManyToManyField(Sexos)
    habilidades = models.ManyToManyField(Habilidades)

    def __str__(self):
        return self.nome
