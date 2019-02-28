from string import ascii_letters


class PokeName():

    def __init__(self, nome_inicial=''):
        self.nome_inicial = nome_inicial
        self.data = {}

    def __get__(self, instance, owner):
        return self.data.get(instance, self.nome_inicial)

    def __set__(self, instance, poke_name):
        if not poke_name.isalpha() or self.tem_caractere_ilegal(poke_name):  # Verifica se o nome do pokémon vai contra as regras de DNS
            self.data[instance] = self.recreate_name(poke_name)
        else:
            self.data[instance] = poke_name
        
    def tem_caractere_ilegal(self, s):
        """Verificação de caractere com acentuação"""

        return any(c not in ascii_letters for c in s)

    def recreate_name(self, poke_name):
        """ Recria o nome do pokemon para que ele esteja de acordo com a norma DNS
        para a url dos sites. Cada Símbolo é substituido por algo diferente e por isso
        foi criado um dicionário.
        """
        dic = {'♀': '-female', '♂': '-male', "'": "", '.': '', ' ': '-', ':': '', 'é': 'e'}

        for special_chars in dic.keys():
            try:  # Tente substiruir, caso não consiga retornará um erro e tentará novamente com outro caractere
                poke_name = poke_name.replace(special_chars, dic[special_chars])
            except:
                continue
        return poke_name
