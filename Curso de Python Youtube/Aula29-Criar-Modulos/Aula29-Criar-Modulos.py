
import modulo as contas

print(contas.soma(5, 5))
print(contas.soma(5, 5, 6))
print(contas.potencia(5, 2))

l1 = [2, 3, 4]
l2 = [2, 5]
print(contas.soma(*l1))
print(contas.potencia(*l2))
print(__name__)
