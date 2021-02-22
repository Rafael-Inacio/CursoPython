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
        self._dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}
        else:
            self._dados['clientes'].update({id: nome})

    def lista_clientes(self):
        print('Exibindo clientes:')
        for id, nome in self._dados['clientes'].items():
            print(f'\t{id}: {nome}')

    def apaga_cliente(self, id):
        del self._dados['clientes'][id]


bd = BaseDeDados()
bd._dados = 'Qualquer coisa'
# ainda é possível acessar e editar o conteúdo da variável e "quebrar" a aplicação

bd.inserir_cliente(1, 'Rafael')
bd.inserir_cliente(2, 'João')
bd.inserir_cliente(3, 'Gil')
bd.lista_clientes()
bd.apaga_cliente(2)
bd.lista_clientes()
