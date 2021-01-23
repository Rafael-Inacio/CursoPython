num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

# isnumeric, isdigit, isdecimal (string methods)
# Números e positivo
print(num1.isnumeric())  # Tem somente número nessa string?
print(num2.isnumeric())

if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    print((num2 + num1))
else:
    print('Não deu para converter os caracteres em números.')


"""
OFF
"""

num3 = input("Entrada num3: ")
num4 = input("Entrada num4: ")


try:
    num3 = int(num3)
    num4 = int(num4)
    print(num3 + num4)
except ValueError:
    print('ERRO!')
