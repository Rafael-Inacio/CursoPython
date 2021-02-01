x = 0  # coluna
y = 0  # linha

while x <= 10:
    y = 0
    while y <= 5:
        print('Coluna {} e linha {}.'.format(x, y))
        y += 1
    x += 1
print('\nAcabou.')
