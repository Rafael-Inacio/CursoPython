""""
Iniciar com letra, pode conter números, separar _, letras minúsculas

"""

nome = 'Josemar'  # string (str)
idade = 10  # interiro (int)
altura = 1.87764  # real (float)
e_maior = idade > 4566  # booleano (bool)

peso = 85

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior que 4566 anos?:', e_maior)

print(idade * altura)

imc = peso/(altura ** 2)
print()
print(nome, 'tem', idade, 'anos de idade e índice de massa corporal (IMC) de', imc)
