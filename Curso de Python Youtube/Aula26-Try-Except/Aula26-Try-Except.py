"""
Tratar exceções
"""

try:  # vai tentar executar o código abaixo, caso de erro entra na exceção
    print(a)
except NameError as erro:
    print('Erro:', erro)
    print('Erro do desenvolvedor, fale com ele.')
except IndexError as erro:  # Erro de índice
    print('Erro:', erro)
except (ValueError, KeyError, FileExistsError) as erro:  # trata de vários erros em uma linha só
    print('Erro:', erro)
except Exception as erro:  # essa linha pega qualquer tipo de erro que ocorrer
    print('Erro:', erro)
    print('Ocorreu um erro inesperado.')
else:  # quando não há erro no código entra no else
    print('Seu código foi executado com sucesso.')
finally:  # sempre será executada
    print('Continua...\n')

print('O código continua...')
