
def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('Log:', error)
        raise  # vai relançar a exceção


try:
    print(divide(2, 0))
except ZeroDivisionError as error:
    print(error)


"""
Lançar minha própria exceção
"""

def divide2(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser zero')
    return n1, n2


try:
    print()
    print(divide2(2, 0))
except ValueError as error:
    print('Erro:', error)

print(divide2(2, 0))
