"""
Ou variável de classe
"""


class A:
    vc = 123  # uma variável da classe, mas pode imprimir está variável utilizando a instância


a1 = A()
a2 = A()

A.vc = 312  # Alterando o valor da variável (ou atributo) da classe

print(a1.vc)
print(a2.vc)
print(A.vc)

print('='*50)
a1.vc = 333  # quando faz isso não está alterando o valor da variável da classe, mas sim criando um atributo direto
# na instância a1

print(a1.vc)
print(a2.vc)
print(A.vc)
