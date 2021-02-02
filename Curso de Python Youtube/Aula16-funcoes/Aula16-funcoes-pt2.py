"""
Funções - def em Python (Parte 2)
"""


def divisao(n1, n2):
    if n2 > 0:
        resultado = n1 / n2
        return resultado


divide = divisao(8, 1)
if divide:
    print(divide)
else:
    print('Conta não válida')


def funcao(var):
    print(var)


variavel = funcao

variavel('Teste')
