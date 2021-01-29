"""
Faça um programa que peça o primeiro nome do usuário. Se o nome conter 4 letras ou menos escreva
"Seu nome é muito curto"; se conter entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6
escreva "seu nome é muito grande".
"""

nome = input('Digite o seu primeiro nome: ')
caracteres = len(nome)

if caracteres <= 4:
    print(f'Seu nome tem {caracteres} letras, é muito curto.')
elif caracteres <= 6:
    print(f'Seu nome tem {caracteres} letras, é normal.')
else:
    print(f'Seu nome tem {caracteres} letras, gigantão.')
