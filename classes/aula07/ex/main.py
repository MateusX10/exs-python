from assoc import Leao, Elefante

elefante1 = Elefante("cinza", 4.50)
leao1 = Leao("amarelo", 1.60)
print(elefante1.cor, elefante1.alt)
print(leao1.cor, leao1.alt)
leao1.cor = elefante1
print(leao1.cor.cor)