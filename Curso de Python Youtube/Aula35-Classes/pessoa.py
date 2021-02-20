"""
Por convenção começa-se uma classe sempre com letra maiúscula
"""


class Pessoa:
    # um método é uma função que pertence à classe
    def falar(self):  # a função falar() é um método da classe Pessoa
        print('A pessoa está falando...')

"""
O (self) serve para referenciar a própria instância que está chamando o métod. Ele aparece em todos os métodos não 
estáticos 
"""
