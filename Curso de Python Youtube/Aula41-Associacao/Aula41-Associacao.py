"""
Relções entre as classes1:
    Associação:
        Uma classe se relaciona com a outra classe, mas nenhuma das duas classes1 dependem uma da outra
"""
from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Rafael')
caneta = Caneta('Jotinha')
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()
