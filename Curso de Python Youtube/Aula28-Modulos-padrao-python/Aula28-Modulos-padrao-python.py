"""
Módulos padrão do Python:
Módulos são arquivos .py (que contém código python) que podem ser importadas para dentro do nosso código
e servem para expandir as funcionalidades padrão da linguagem.
"""
# Por exemplo, se quisermos saber em qual plataforma o python está rodando podemos usar o módulo sis
import sys
from sys import platform  # Importa algo específico de um módulo
from sys import platform as os  # Importa algo e "dá um apelido"
import random  # para gerar números aleatórios


print(sys.platform)
print(platform)
print(os)

# gerar um número inteiro aleatório entre 1 e 10
print(random.randint(1, 10))
