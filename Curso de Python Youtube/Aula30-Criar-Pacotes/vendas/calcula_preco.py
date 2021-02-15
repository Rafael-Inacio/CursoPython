import formata.formata_preco


def aumento(valor, porcentagem, formatado=False):
    resultado = valor * (1 + porcentagem/100)
    if formatado:
        return formata.formata_preco.real(resultado)
    else:
        return resultado


def desconto(valor, porcentagem, formatado=False):
    resultado = valor * (1 - porcentagem/100)
    if formata:
        return formata.formata_preco.real(resultado)
    else:
        resultado


if __name__ == '__main__':
    print(aumento(50, 10, formatado=True))
    print(desconto(50, 10, formatado=True))

