"""
len(), não funciona com tipos numérios

"""
usuario = input('Digite o seu usuário: ')
qtd_caracteres = len(usuario)

# lun retorna a quantidade de caracteres em uma variável do tipo inteiro
print(usuario, qtd_caracteres, type(qtd_caracteres))
print()
if qtd_caracteres < 6:
    print('O usuário precisa ter pelo menos 6 caracteres')
else:
    print('Ok')
