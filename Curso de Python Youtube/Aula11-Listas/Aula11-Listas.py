"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

lista = ['A', 'B', 'C', 12, 23.3, True, False]  # Pode-se colocar valores de diversos tipos
print()

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print(l3)

l1.extend(l2)
l1.append('a')
print(l1)

# Criação de uma lista de números usando range()
l4 = list(range(1, 20, 2))
print(l4)
