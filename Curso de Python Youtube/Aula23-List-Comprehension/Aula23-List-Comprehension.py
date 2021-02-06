"""
Compreensão de listas
Usadas para otimização e diminuir o tamanho do código
"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8]
ex1 = [variavel for variavel in l1]
ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(3)]

print(ex1)
print(ex2)
print(ex3)

l2 = ['Rafael', 'Maria', 'Paula', 'Amanda']
ex4 = [v.replace('a', '@') for v in l2]
print(ex4)

# Filtrar valores em listas

l3 = list(range(100))
# filtrar todos os números da lista que são divisíveis por 2
ex5 = [v for v in l3 if v % 2 == 0]
print(ex5)
# filtrando todos que são divisíveis por 3 e 8
ex6 = [v for v in l3 if v % 3 == 0 and v % 8 == 0]
print(ex6)
# usando else
ex6 = [v if v % 3 == 0 and v % 8 == 0 else '_' for v in l3]
print(ex6)
