"""
Entrada de dados

"""

# input() sempre dá uma variável do tipo str
nome = input('Qual é o seu nome? ')

# É possível converter a entrada.
idade = int(input('Qual a sua idade? '))

# Ou converter a variável depois de atribuída
idade = int(idade)

ano_nasc = 2021 - idade
print()
print(f'O usuário digitou {nome} e o formato da variável é {type(nome)}')

print()
print(f'O ano de nascimento é {ano_nasc}')

