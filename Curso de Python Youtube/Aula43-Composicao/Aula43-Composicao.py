"""
Relções entre as classes:
    Agragação:
        Uma classe vai ser dona de objetos de outras classes
"""
from classes2 import Cliente

c1 = Cliente('Rafael', 65)
c2 = Cliente('Jaime', 77)

c1.insere_endereco('Vermelhandia', 'PR')
c1.insere_endereco('Rio de Janeiro', 'RJ')
c2.insere_endereco('Tangamandápio', 'AP')
c1.listar_enderecos()
c2.listar_enderecos()
