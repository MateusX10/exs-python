from pessoas import Pessoa

p1 = Pessoa("Henrique", 19, 68.5, 1.70)
p2 = Pessoa("Fanis", 14, 48, 1.48)

print(f'{p1.nome}, {p1.idade} anos, {p1.peso} Kg, {p1.altura} m')
print(f'{p2.nome},  {p2.idade} anos, {p2.peso} Kg, {p2.altura} m')
p1.envelhecer(5)
p1.crescer(10)
print(p1.engordar(10))
print(p1.emagrecer(5))