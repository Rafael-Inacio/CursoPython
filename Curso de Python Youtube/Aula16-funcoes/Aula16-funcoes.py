"""
Funções - def em Python (Parte 1)
"""


def funcao():
    print('Olá Mundo')


def funcao2(msg):
    print(msg)

# função com parâmetros padrões


def saudacao(msg='Olá', nome='usuário'):
    print(msg, nome)


funcao()
funcao()
funcao()
funcao()

m = 'Olá'

funcao2(m)
funcao2(m)
funcao2(m)
funcao2('\nTeste\n')

saudacao()
saudacao('Olá', 'Rafael')
saudacao(nome='Renanzinho')

print('\nHello World')
print('Hello World')
print('Hello World')
print('Hello World')
