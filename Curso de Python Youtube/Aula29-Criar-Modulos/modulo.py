

def potencia(n1, n2):
    return n1 ** n2


def soma(*args):
    soma = 0
    for i in args:
        soma += i
    return soma


# print(__name__)
if __name__ == '__main__':  # para quando eu importar este módulo em outro código a parte de baixo não seja executada.
    # Todos cógigos python que está sendo executado atualmente se chama '__main__', por isso o código abaixo só
    # será executado quando este arquivo (modulo.py) for executado. Quando este arquivo (modulo.py) é importado em
    # outro código deixa de ter o nome '__main__' e passa a ter o nome do arquivo .py, neste caso 'modulo'.
    l1 = [2, 4, 5, 6]
    print(potencia(2, 3))
    print(soma(*l1))
    print(soma(2, 3, 5))
