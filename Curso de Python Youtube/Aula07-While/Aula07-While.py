"""
while em Python - Aula 7
utilizado para realizar ações enquanto
uma condição for verdadeira.

while condição:
    'código'
"""
# while True:  # loop infinito
#     nome = input('Qual o seu nome? ')
#     print('Seu nome é: ', nome)
#
# print('Não será executado.')  # Nunca será executada

#############################
#############################
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue  # volta para o início do laço, pula o código que estiver abaixo
        # break  #  break, diferente do 'continue' faz com que o interpretador "saia" do loop, o break finaliza
        # o loop ou laço

    print(x)
    x += 1
print('Acabou')
