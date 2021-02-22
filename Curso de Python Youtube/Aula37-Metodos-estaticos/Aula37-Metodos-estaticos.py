from random import randint

class Pessoa:
    ano_atual = 2021  # Isto é um atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nasc(self):
        print(self.ano_atual - self.idade)

    # criando método de classe. Antes criamos métodos de instâncias.

    @staticmethod  # Não precisa da instância nem da classe
    # "Uma função normal", mas que por questão de organização precisa estar dentro da classe
    def gera_id():  # Não recebe self nem cls, mas pode receber outros parâmetros.
        rand = randint(10000, 19999)
        return rand


p1 = Pessoa('Rafael', 27)
print(p1.nome, p1.idade)
p1.ano_nasc()
print('='*50)
print(p1.gera_id())
