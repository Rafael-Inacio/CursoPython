"""
Split - Dividir uma string # str
Join - Juntar uma lista # str
Enumerate - Enumerar elementos da lista # list / Para objetos iteráveis
"""

string = 'O rato roeu a roupa do rei pelé'
lista = string.split(' ')
print(lista)

# Join
lista_join = ['Rafael', 'Inacio', 'Luke', 'João']
string_juntada = ' '.join(lista_join)
print(string_juntada)

# Enumerate
for indice, valor in enumerate(lista_join):
    print(indice, valor)


# Faz o mesmo que o for de cima, só que sem usar enumerate
lista2 = [
    [0, 'Rafael'],
    [1, 'Inacio'],
    [2, 'Luke'],
    [3, 'João']
]
print('{:#^20}'.format(''))
for indice, valor in lista2:
    print(indice, valor)
