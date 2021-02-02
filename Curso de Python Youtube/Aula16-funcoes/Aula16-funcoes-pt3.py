"""
Funções - def em Python (Parte 3) - *args **kwargs

*args - quando não sei quantos argumentos vão na chamada da função. É basicamente um empacotamento
e um desempacotamento ao mesmo tempo

**kwargs - Keyword arguments - Argumentos nomeados

"""


def func(*args, **kwargs):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))
    print(kwargs)
    print(kwargs['teste'])
    print('=============')


func(1, 2, 3, 4, 'Rafael', False, None, teste='Nome')

lista = [1, 2, 3, 'Rafael']
func(*lista, teste='Rafael')

