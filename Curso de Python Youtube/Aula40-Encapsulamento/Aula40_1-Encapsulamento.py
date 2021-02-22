"""
Em programação orientada a objetos o encapsulamento serve para esconder certas partes do código, para proteger a
aplicação, proteger a classe.

No exemplo abaixo uma linha do tipo:
    bd.dados = 'Qualquer coisa'

O atributo self.dados está como público, desprotegido, acessível de fora da classe

Conveção:
    _: 1 (um) underline. '"private" é privado entre aspas, pois ainda consegue-se acessar e editar'.
        bd._dados = 'Qualquer valor'

    __: 2 (dois) underline. 'Um privado mais forte'.
        bd._NOMEDACLASSE__dados = 'Qualquer outro valor'
"""


class BaseDeDados:
    def __init__(self):
        self.dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})

    def lista_clientes(self):
        print('Exibindo clientes:')
        for id, nome in self.dados['clientes'].items():
            print(f'\t{id}: {nome}')

    def apaga_cliente(self, id):
        del self.dados['clientes'][id]


bd = BaseDeDados()
# bd.dados = 'Qualquer coisa'
bd.inserir_cliente(1, 'Rafael')
bd.inserir_cliente(2, 'João')
bd.inserir_cliente(3, 'Gil')
bd.lista_clientes()
bd.apaga_cliente(2)
bd.lista_clientes()
