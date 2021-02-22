"""
Relções entre as classes1:
    Agragação:
        Uma classe usa outra classe como parte de si e essa classe precisa da outra classe
"""

from classes1 import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()
p1 = Produto('Camiseta', 50)
p2 = Produto('Iphone', 10000)
p3 = Produto('Caneca', 15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)

carrinho.listar_produtos()

print(carrinho.soma_total())
