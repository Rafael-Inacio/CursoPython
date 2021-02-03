variavel = 'Um valor'  # variável global, acessível de todos os locais


def func():
    print(variavel)


def func2():
    variavel = 'Outro valor'  # Este valor será alterado apenas dentro da função func2(). Na verdade é outra variável
    # criada dentro da func2()
    print(variavel)


def func3():
    global variavel  # Agora está variável é a mesma que aquela no começo do código. "Editar variáveis globais
    # dentro de funções não é uma boa. Pode gerar comportamentos estranhos."
    variavel = 'Outro Valor2'
    print(variavel)


func()
func2()
func3()
func()
