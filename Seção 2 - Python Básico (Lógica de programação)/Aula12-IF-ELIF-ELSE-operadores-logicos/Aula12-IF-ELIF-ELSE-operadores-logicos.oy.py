"""
Condições IF, ELIF e ELSE

OPERADORES LÓGICOS
and, or, not, in e not in

"""

a = 2
b = 2
c = 3

res = (a == b) and b < c
print(res)

print(a < c and b < c)

print(a == b or b == c)

print(not(a == b or b == c))

# Usa-se o not, também, para verificar valores vazios (tanto int e float quanto string)

a = 0
if not a:
    print('Por favor insira um valor para "a"')
else:
    print('"a" vale {a}')


nome = 'Rafael'
if 'a' in nome:
    print(f'Existe a letra "a" em {nome}')
else:
    print(f'Não existe a letra "a" em {nome}')
