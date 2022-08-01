from cla import Pessoa

p1 = Pessoa("Miguel", 30)
print(p1.nome, p1.idade)
print(p1.get_ano_nascimento())
print(p1.gera_id())
print(Pessoa.gera_id())