"""
Perguntas e respostas usando dicionários
"""
respostas_corretas = 0
perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'alternativas': {'a': '1', 'b': '2', 'c': '3', 'd': '4'},
        'resposta_certa': 'd'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3+2?',
        'alternativas': {'a': '1', 'b': '2', 'c': '5', 'd': '4'},
        'resposta_certa': 'c'
    },
}
for perguntas_keys, perguntas_values in perguntas.items():
    print(perguntas_keys, perguntas_values['pergunta'], sep=': ')

    for alternativas1, alternativas2 in perguntas_values['alternativas'].items():
        print('\t [{}]: {}'.format(alternativas1, alternativas2))
    print()
    resposta = str(input('Qual é a repostas correta? ')).lower()

    if resposta == perguntas_values['resposta_certa'].lower():
        print('Certa resposta. A alteranativa correta é a alternativa {}.'.format(perguntas_values['resposta_certa']))
        respostas_corretas += 1
    else:
        print('Escolheu a alternativa incorreta. A alternativa correta é a {}'
              .format(perguntas_values['resposta_certa']))
    print()
print()
qt_perguntas = len(perguntas)
porcentagen_acertos = respostas_corretas / qt_perguntas * 100
print('Você acertou {} de {}, isto é {}% das perguntas.'.format(respostas_corretas, qt_perguntas, porcentagen_acertos))
