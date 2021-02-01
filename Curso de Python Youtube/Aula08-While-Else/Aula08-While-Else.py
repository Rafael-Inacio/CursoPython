"""
While / Else - Aula 08
Contadores
Acumuladores

"""

contador = 1
acumulador = 1

while contador < 100:
    print(contador, acumulador)
    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else.')
