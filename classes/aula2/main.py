from pessoas import Pessoa


p1 = Pessoa.por_ano_nascimento("Luís", 2002)
p2 = Pessoa.por_ano_nascimento("Mateus", 1982)
p3 = Pessoa("Alan", 10)
print(p1)
print(p2)
print(p3)
print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
print(p3.get_ano_nascimento())
