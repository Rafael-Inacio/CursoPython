
palavra = 'Carregador'
palavra_temp = ''
letras_tentadas = []
letras_tentadas_certas = []
tentativas = 3

while tentativas > 0:

    print()
    print('Você tem {} tentativas'.format(tentativas))
    escolha = input('Digite uma letra para que você acha que faz parte da palavra: ')
    print()
    escolha = escolha.strip().lower()
    palavra = palavra.strip().lower()

    if len(escolha) > 1 and escolha not in letras_tentadas:
        print('Não, isso não vale. Por favor digite apenas uma letra.')
        continue
    elif not escolha.isalpha() and escolha not in letras_tentadas:
        print('Por favor, digite apenas uma letra. Número não pode.')
        continue
    elif escolha in letras_tentadas:
        print('Essa letra você já tentou. Tente outra.')
        continue
    else:

        if escolha in palavra:
            print('ACERTOOOU! Você acertou uma letra.')
            palavra_temp = ''
            letras_tentadas.append(escolha)
            letras_tentadas_certas.append(escolha)
            for letra in palavra:
                if letra in letras_tentadas_certas:
                    palavra_temp += letra
                else:
                    palavra_temp += '*'
        else:
            print('ERROOOU! Tente novamente.')
            letras_tentadas.append(escolha)
            tentativas -= 1

        print(palavra_temp)

    if palavra_temp == palavra:
        print('PARABÉNS! Você ganhou, a palavra é {}.'.format(palavra))
        break

if palavra_temp != palavra:
    print()
    print('PERDEU! Você não tem mais nenhuma tentativa.')
