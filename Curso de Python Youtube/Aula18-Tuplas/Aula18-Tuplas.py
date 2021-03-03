"""
Tuplas são bem parecidas com lista, a diferença é que a tupla não é editável, mas é possível converter tuplas para
listas e vice-versa.
"""

t1 = (1, 2, 'Olá')
t2 = 1, 3, 'Rafael'
t3 = 1,

l1 = list(t1 + t2)

t4 = t1 + t2

print(t1, type(t1))
print(t2, type(t2))
print(t3, type(t3))
print(t4)


for valor in t1:
    print(valor)

print(l1, type(l1))
print(tuple(l1), type(tuple(l1)))
