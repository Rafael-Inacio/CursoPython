"""
For também suporta else e While/Else também

"""
lista = ['Rafael', 'Paula', 'The Walking Dead', 'Malhação']

for n in lista:
    if n.lower().startswith('s'):
        break
else:
    print('Nenhuma das palavras comçam com "s"')
