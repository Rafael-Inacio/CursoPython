
nome = 'Edison Era Antes do Nascimento'
idade = 65
altura = 1.986564
gols = 15000

print(nome, 'tem',altura, 'metros de altura,', idade, 'anos de idade e fez', gols, 'gols em toda sua carreira.\n')
print(f'{nome} tem {altura:.2f} metros de altura, {idade} anos de idade e fez {gols} gols em toda sua carreira\n')
print('{} tem {:.2f} metros de altura, {} anos de idade e fez {} gols em toda sua carreira\n'.format(nome, altura, idade,
                                                                                                   gols))
# Se for repetir as variáveis pode-se fazer o seguinte:
print('{0} tem {1} metros de altura, {2} anos de idade e fez {3} gols em toda sua carreira. TESTE {3} {3} {1} {0}\n'
      .format(nome, altura, idade, gols))
# Pode-se, também, nome as variáveis
print('TESTE = {g}, {n}, {a}, {a}, {i}'.format(n=nome, a=altura, i=idade, g=gols))
