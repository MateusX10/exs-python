from pontoret import Ponto, Retangulo

ponto1 = Ponto(10.5, 8.9)
ret1 = Retangulo(8, 5)
ret2 = Retangulo(18, 12)
ret3 = Retangulo(15, 10)
ret1.menu()
ret2.menu()
ret3.menu()
figuras = [ret1, ret2, ret3]

print(f'X: {ponto1.x} Y: {ponto1.y}')
for figura in figuras:
    print(f'Largura: {figura.larg} cm, altura: {figura.alt} cm')
for el in figuras:
    print(f'{el.centro()}cm')
