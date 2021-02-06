"""
Iteráveis:
    Lista é um objeto iterável


Um iterável é um objeto que se pode iterar sobre ele mas ele não é necessariamente um iterador
Uma lista grande ocupa muito mais espaço na memória do que a mesma lista do tipo lista geradora
"""
import sys

lista = [0, 1, 2, 3, 4, 5]
print(hasattr(lista, '__iter__'))  # verifica se é iterável
for v in lista:  # este for transforma a lista em um iterador
    print(v)

print(hasattr(lista, '__next__'))  # verifica se é um iterador
lista = iter(lista)
print(hasattr(lista, '__next__'))  # Agora a lista é um iterador
print()
print(next(lista))
print(next(lista))
print(next(lista))

lista2 = list(range(10))

l1 = [v for v in range(10000)]
print(type(l1), sys.getsizeof(l1))
l2 = (v for v in range(10000))
print(type(l2), sys.getsizeof(l2))
