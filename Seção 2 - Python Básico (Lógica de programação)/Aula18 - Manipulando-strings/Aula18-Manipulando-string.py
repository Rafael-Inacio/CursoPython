"""
Manipulando strings
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

"""

texto = 'Python'
print(texto[2])  # Deve ter como saída o 't'
print(texto[-2])  # Deve ter como saída o 'o'

nova_string = texto[2:5]
print(nova_string)
nova_string2 = texto[::2]  # Passo, pula de 2 em 2
print(nova_string2)
