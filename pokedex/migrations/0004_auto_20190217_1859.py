# Generated by Django 2.1.7 on 2019-02-17 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_auto_20190215_1814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemons',
            old_name='descrição',
            new_name='descricao',
        ),
    ]
