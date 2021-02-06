# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)

# diferença entre conjutos e dicionários é que o conjunto não tem par chaves-valores, apenas valores
# Os conjuntos não respeitam ordem, cada momento pode aparecer em uma ordem diferente da criada
s1 = {1, 2, 3, 4, 5, 'Rafael'}
s2 = set()
s2.add(5)
s2.add((87, 13, 25, 'José'))
s2.add('Inacio')

print(s1)
print(s2)

s2.discard(5)
s2.update('a')  # similar a .add() vai adiconar o 'a'
s2.update('Python')  # vai iterar letra por letra no conjunto
s2.update([1, 2, 'Rafa'])

print(s2)


# remover elementos ducplicados de uma lista
l1 = [1, 1, 1, 2, 3, 4, 5, 6, 5, 5, 5, 5, 4, 4, 4, 4, 'Rafael', 'Rafael']
l1 = set(l1)
print(l1)
l1 = list(l1)
print(l1)

s10 = {1, 2, 3, 4, 5, 8}
s11 = {1, 2, 3, 4, 5, 6, 7}
print()
s20 = s10 | s11  # união
print(s20)
s21 = s10 & s11  # interseção
print(s21)
s22 = s11 - s10  # diferença
print(s22)
s23 = s10 ^ s11  # dierença simétrica
print(s23)


# Verificar se uma lista contém outra lista
l2 = ['Rafael', 'João', 'Maria', 'Maradona']
l3 = ['Rafael', 'João', 'Maria', 'Maradona', 'Rafael', 'Maria']  # Esta lista é diferente de l2, mas contém todos
# os elementos de l2. Se uma das listas tiver um elemento que não está presente na outra a verificação de baixo falha.

# checagem

print(set(l2) == set(l3))

# Checagem com lista que contém a outra mas tem elementos diferentes
l4 = l3 + ['Edison']
# l2 = l2 + ['Edison', 'Pelé']
print(set(l2) == set(l4))  # vai falhar

print('Lista L2 {}'.format(l2))
print('Lista L4 {}'.format(l4))

intersecao = set(l2) & set(l4)  # interseção dos conjuntos l2 e l4
if intersecao == set(l4):
    print('A lista L4 está contida na lista L2 , isto é, todos os elementos da lista L4'
          ' está presente na lista L2.')
elif intersecao == set(l2):
    print('A lista L2 está contida na lista L4, isto é, todos os elementos da lista L2'
          ' está presente na lista L4.')
else:
    print('As listas L2 e L4 não estão contidas uma na outra.')
