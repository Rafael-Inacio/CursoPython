"""
* Nas listas o python gera os índices, no dicinário o programador controla o índice (também chamado de cahve)
* Chaves precisam ser únicas
"""

d1 = {'chave1': 'Valor da chave'}
print(d1)
d1['nova_chave'] = 'Valor da nova chave'
print(d1)
print(d1['chave1'])

# Outra forma de criar dicionários
d2 = dict(chave1='Valor da chave1', chave2='Valor da chave2')
print(d2)


d1.update({'nova_chave2': 'Novo valor'})
if d1.get('nova_chave2'):
    print(d1['nova_chave'])

del d1['chave1']  # Apagar um item do dicionário
print(d1)

print()
print('nova_chave' in d1)
print('nova_chave' in d1.keys())  # Mesma coisa que a linha de cima
print('Valor da nova chave' in d1.values())

print('O dicionário d1 tem {} pares de chave e valor'.format(len(d1)))
print()
for i in d1.items():
    print(i)
print()
for k, v in d1.items():
    print(k, v)
