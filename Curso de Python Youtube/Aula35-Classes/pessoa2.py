"""
Por convenção começa-se uma classe sempre com letra maiúscula
"""
"""
O (self) serve para referenciar a própria instância que está chamando o métod. Ele aparece em todos os métodos não
estáticos
"""


class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade, comendo=False, falando=False):  # "Um método especial".
        self.nome = nome  # Essas variáveis estão disponíveis para todos os métodos dentro dessa classe
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def outro_metodo(self):
        print('Inicializando outro método...')
        print(self.idade)

    def comer(self, alimento):
        if self.comendo is False:
            print(f'{self.nome} está comendo {alimento}')
            self.comendo = True  # Altera o estado da variável
        else:
            print(f'{self.nome} já está comendo.')

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
        else:
            print(f'{self.nome} parou de comer.')
            self.comendo = False

    def falar(self, assunto):
        if self.nome.lower() in 'Jair Bolsonaro'.lower():
            if self.comendo:
                print(f'{self.nome} está falando merda enquanto come.')
                return
            elif self.falando:
                print(f'{self.nome} já está falando merda. Não dá ideia.')
                return
            else:
                print(f'PQP o {self.nome} começou a falar merda. PQP!!!!')
                self.falando = True
                return
        if self.comendo:
            print(f'{self.nome} não pode falar enquanto está comendo.')
        elif self.falando:
            print(f'{self.nome} já está falando.')
        else:
            print(f'{self.nome} está falando sobre {assunto}.')
            self.falando = True

    def ano_nasc(self):
        return self.ano_atual - self.idade
