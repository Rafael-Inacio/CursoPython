
file = open('arquivo.txt', 'w+')  # Se o arquivo não existe ele vai ser criado.
file.write('Linha 1\n')
file.write('Linha 2\n')
file.seek(0, 0)  # volta o cursor para o começo do arquivo
print('Lendo o arquivo:')
print(file.read())  # lendo o arquivo inteiro
file.seek(0, 0)
print('Lendo linha por linha:')
print(file.readline(), end='')
print(file.readline())

file.seek(0, 0)
print('Todas as linhas em uma lista:')
print(file.readlines())
file.close()

