"""
Expressões lambda ou Funções anônimas

Quando precisa passar uma função para outra função ou método, se for simples pode-se usar as expressões lambda para isso
"""
v1 = 2
v2 = 3


def funcao(arg1, arg2):
    return arg1 * arg2


var = funcao(v1, v2)
print(var)

a = lambda x, y: x * y

print(a(v1, v2))

#######################
# USO
lista = [
    ['P1', 13],
    ['P2', 7],
    ['P3', 23],
    ['P4', 52],
    ['P5', 17]
]
# ordenar a lista de listas pelo preço


def func(item):
    return item[1]


lista.sort(key=func, reverse=True)
print(lista)

# OU

lista.sort(key=lambda item: item[1])
print(lista)

# OU

print(sorted(lista, key=lambda i: i[1], reverse=True))

