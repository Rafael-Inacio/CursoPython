"""
Formatando valores com modificadores

:s - Texto (string)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num1 = 10
num2 = 3
divisao = num1 / num2

print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

print()
nome = 'Rafael Inacio'
print(f'{nome:s}')

print()
print(f'{num2:0>2}')
print(f'{num1:0>2}')
print(f'{num2:0>3}')
print(f'{num1:0>3}')
print(f'{num2:0>10.2f}')
print(f'{num1:0>10.2f}')

print()
print(f'{nome:#^50}')

nome_formatado = '{:@^50}'.format(nome)
print()
print(nome_formatado)
