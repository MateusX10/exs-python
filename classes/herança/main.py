from cliente import *

'''Associação - usa | agregação - tem | composição - é done | herança - é'''    

c1 = Cliente("Ronaldinho", 35)
a1 = Aluno("Vinícios", 12)
p1 = Pessoa("Mauro", 78)
print(f'Nome do cliente: {c1.nome}, idade: {c1.idade} anos')
print(f'Nome do aluno: {a1.nome}, idade: {a1.idade} anos')
c1.falar()
a1.falar()
c1.correr()
a1.correr()
c1.parar()
a1.parar()
c1.comprar()
a1.estudar()

p1.falar()
p1.andar()
