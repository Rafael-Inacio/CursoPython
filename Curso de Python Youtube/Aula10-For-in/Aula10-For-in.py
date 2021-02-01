"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)

"""

texto = 'Python'
nova_string = ''

for letra in texto:
    print(letra)

print()

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)
print()


for n, letra in enumerate(texto):
    print(n, letra)

print()

for n in range(10):
    print(n)

print()

for n in range(1, 10, 2):
    print(n)


