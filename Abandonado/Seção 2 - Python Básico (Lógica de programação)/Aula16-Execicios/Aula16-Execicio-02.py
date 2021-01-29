"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação
apropriada
"""

hora = input('Digite a hora (H) atual, sem os minuros ou segundos (0-23): ')

if hora.isnumeric() and int(hora) < 25:
    hora = int(hora)
    if hora <= 11:
        print(f'Agora são {hora} horas. Bom dia!')
    elif hora <= 17:
        print(f'Agora são {hora} horas. Boa tarde!')
    elif hora <= 23:
        print(f'Agora são {hora} horas. Boa noite!')
else:
    print('Você não digitou um valor válido para hora.')
