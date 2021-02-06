lista = [
    ('chave', 2),
    ('chave2', 'valor2'),
]

d1 = {x: y for x, y in lista}
print(d1)
# mesma coisa do de cima
d2 = dict(lista)
print(d2)

# mudando valores
d3 = {x.upper(): y * 2 for x, y in lista}
print(d3)

# compreensão de conjuntos (set)
s1 = {x for x in range(6)}
print(s1, type(s1))
