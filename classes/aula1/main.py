from pessoas import Pessoa


p1 = Pessoa("Guilherme", 30)
p2 = Pessoa("Arnaldo", 40)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
p1.comer("ALFACE")
p1.PararComer()
p1.falar()
p1.PararFalar()
p2.falar()
p2.PararFalar()
p2.comer()
p2.PararComer()
print(p1.ano_atual)
print(p2.ano_atual)
print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
print(p1.por_ano_nascimento("Guilherme", ))