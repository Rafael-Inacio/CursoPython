"""
* Criar variáveis para nome (str), idade (int), altura (float) e peso (float) de uma pessoa
* Criar variável com ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chavves)
"""
nome = 'Arthur da Vó'
idade = 45
altura = 1.25
peso = 235
ano_atual = 2053

# Começa os cálculos
nasc = ano_atual - idade
imc = peso / altura ** 2

print('{} tem {} anos de idade, {} de altura e pesa {}kg.'.format(nome, idade, altura, peso))
print('O IMC do {} é de {:.2f}.'.format(nome, imc))
print('{} nasceu em {}.'.format(nome, nasc))
