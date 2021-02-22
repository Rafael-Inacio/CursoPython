"""
Quando usar métodos de classe e métodos de instância?
    Pense: esse método é relacionado à classe em geral ou à instância?
Um método que "Fabrica o objeto"

"""


class Pessoa:
    ano_atual = 2021  # Isto é um atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nasc(self):
        print(self.ano_atual - self.idade)

    # criando método de classe. Antes criamos métodos de instâncias

    @classmethod  # Adiantando: isso é um decorador que decora o método abaixo
    def por_ano_nascimento(cls, nome, ano_nascimento):  # 'cls'(pode ser qualquer nome, mas por convenção usa-se 'cls')
        # refere-se à classe, não à instância 'self' como antes
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)  # retornando o objeto da classe. "Fabrica o objeto"


p1 = Pessoa('Rafael', 27)
print(p1.nome, p1.idade)
p1.ano_nasc()
print('='*50)
p2 = Pessoa.por_ano_nascimento('Rafael', 1994)
print(p2.nome, p2.idade)
p2.ano_nasc()
