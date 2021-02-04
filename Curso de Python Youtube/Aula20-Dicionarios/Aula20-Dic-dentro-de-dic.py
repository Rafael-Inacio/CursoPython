clientes = {
    'cliente1': {'nome': 'Rafael',
                 'sobrenome': 'Inacio'},
    'cliente2': {'nome': 'Jacaré',
                 'sobrenome': 'Vacinado'}
}

for clientes_k, clientes_v in clientes.items():
    print('Exibindo {}'.format(clientes_k))
    for dados_k, dados_v in clientes_v.items():
        print('\t {} = {}'.format(dados_k, dados_v))
    print()
