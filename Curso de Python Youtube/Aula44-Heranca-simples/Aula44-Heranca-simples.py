"""
Relções entre as classes:
    Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""

from classes3 import Cliente, Aluno

c1 = Cliente('Rafael', 12)
c1.falar()
c1.comprar()

print()
a1 = Aluno('Rafael', 44)
a1.falar()
a1.estudar()
