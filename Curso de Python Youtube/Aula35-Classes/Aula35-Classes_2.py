from pessoa2 import Pessoa

p1 = Pessoa('Rafael', 98)
p2 = Pessoa('João', 19)

p1.outro_metodo()

p1.comer('Alface')
p1.comer('grama')
p1.parar_comer()
p1.parar_comer()
p1.comer('grama')
p1.falar('POO')
p1.parar_comer()
p1.falar('POO')
p1.falar('POO')
p2.falar('jogos')
print("="*50)

print(p1.ano_atual)
print(p2.ano_atual)
print(Pessoa.ano_atual)
print()
print(p1.ano_nasc())
print(p2.ano_nasc())
