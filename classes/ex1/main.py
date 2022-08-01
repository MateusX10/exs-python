from bola import Bola

bola1 = Bola("preto", "22 cm", "couro sintético")
bola2 = Bola("azul", "15 cm", "couro natural")

print(bola1.cor, bola1.circunferencia, bola1.material)
print(bola2.cor, bola2.circunferencia, bola2.material)
bola1.MostrarCor()
bola1.TrocarCor()
print(bola1.cor)
bola2.MostrarCor()
bola2.TrocarCor()
bola2.MostrarCor()
