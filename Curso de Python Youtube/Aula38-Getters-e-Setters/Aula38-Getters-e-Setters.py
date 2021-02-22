"""
O getter obtém o valor e o setter configurado este valor

Funciona como se fosse um filtro, uma proteção para validar os campos
"""


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco * (1 - percentual / 100)

    # Getter
    @property  # decorador prorpiedade
    def preco(self):
        return self._preco  # O nome da variável pode ser qualquer um, mas convencionalmente usa-se o nome da variável
        # seguida de underline (_)

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))  # caso específico, se for utilizado a string de outra forma
            # ('R$ 14', 'RS14', 'r$ 14,3' etc) continuaria dando erro. Para contornar poderia usar expressões regulares
            # que vai ser vista posteriormente no curso.
        self._preco = valor


p1 = Produto('Camiseta', 50)
p1.desconto(10)
print(p1.preco)

# um problema que pode acontecer é que espera-se um preço como inteiro, mas pode vir como string
# Seria ruim alterar o código depois de muita coisa já feita. Ai que entra o os getters e setters
p2 = Produto('Caneca', 'R$15')
p2.desconto(10)
print(p2.preco)

