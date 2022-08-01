from funcoes import *

func1 = Funcionario("Fernando", 22)
p1 = Pessoa("Amanda", 99)

func1.definir_salario(1350)
print(func1.nome, func1.idade, func1.salario)
print(func1.aumento(45))
print(func1.diminui(15))

print(p1.nome)
print(p1.idade)