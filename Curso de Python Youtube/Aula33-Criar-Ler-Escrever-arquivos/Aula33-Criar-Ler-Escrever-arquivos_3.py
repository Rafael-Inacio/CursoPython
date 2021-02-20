"""
Abrindo arquivos com gerenciadores de contexto.
Desta forma não precisa fechar o arquivo no final da execução
"""

with open('arquivo.txt', 'w+') as file:
    file.write('Linha 01\n')
    file.write('Linha 02\n')
    file.write('Linha 03\n')
    file.seek(0, 0)
    print(file.read())

# No append mode 'a' ou 'a+', o cursor é jogado para o final do arquivo. Novos textos não apagarão os texto existentes.
with open('arquivo.txt', 'a+') as file:
    file.write('Outra linha\n')
    file.seek(0, 0)
    print(file.read())
