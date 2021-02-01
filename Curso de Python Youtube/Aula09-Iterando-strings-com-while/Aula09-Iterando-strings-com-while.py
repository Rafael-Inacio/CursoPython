"""
A string é imutável, não posso alterar uma letra da string, mas posso alterar todo o valor da variável

"""

minha_string = 'O rato roeu a roupa do rei de roma.'
comprimento_string = len(minha_string)
contador = 0

nova_string = ''

while contador < comprimento_string:

    if minha_string[contador] == 'r':  # Mudar os 'r's para maiúsculos
        nova_string = nova_string + minha_string[contador].upper()
    else:
        nova_string = nova_string + minha_string[contador]
    #
    # print(minha_string[contador])
    contador += 1

print(nova_string)
print(nova_string.count('R'))  # quantas vezes occore 'R' na string
