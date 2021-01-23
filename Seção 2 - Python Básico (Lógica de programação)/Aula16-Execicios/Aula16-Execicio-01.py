"""
Faça um programa que peça ao usuário para digitar um número inteiro, infome se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""


num = input('Digite um número inteiro: ')

print()


if num.isnumeric():
    num = int(num)
    if num % 2 == 0:
        print(f'O número {num} é um número inteiro e par.')
    else:
        print(f'O número {num} é um número inteiro e ímpar')
else:
    print('Por favor, insira um número inteiro.')
