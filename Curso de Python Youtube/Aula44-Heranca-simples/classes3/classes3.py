class Pessoa:  # Esta classe é chamada de superclasse
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando..')


class Cliente(Pessoa):  # Esta classe é chamada de subclasse
    def comprar(self):
        print(f'{self.nomeclasse} está comprando...')


class Aluno(Pessoa):  # Esta classe é chamada de subclasse
    def estudar(self):
        print(f'{self.nomeclasse} está estudando...')
