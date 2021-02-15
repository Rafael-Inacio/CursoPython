"""
Exemplo um dódigo de uma loja virtual

Tive que marcar as pastas "Aula30..." e "vendas" como "Source" para rodar o código, antes disso eu tinha erro de
importação dos módulos
"""
import vendas.calcula_preco

produto = 49.90
valor_com_aumento = vendas.calcula_preco.aumento(produto, 15, formatado=False)
valor_com_desconto = vendas.calcula_preco.desconto(produto, 15, formatado=True)

print(valor_com_aumento)
print(valor_com_desconto)

