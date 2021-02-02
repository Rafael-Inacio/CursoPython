"""
Desempacotamento de listas em Python

"""

lista = ['Rafael', 'Inacio', 'Luke', 'João']
n1, n2, n3, n4 = lista

n01, n02, *outra_lista = lista

n001, *outra_lista2, ultimo_valor = lista

print(n3)
print(n02)
print(outra_lista)
print(outra_lista2)
print(ultimo_valor)
