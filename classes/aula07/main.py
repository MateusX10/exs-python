from associacao import Escritor, Caneta, MaquinaEscrever

escritor1 = Escritor("Bernardo")
caneta1 = Caneta("bic")
maquina1 = MaquinaEscrever()
print(escritor1.nome)
print(caneta1.marca)
print(maquina1)
print(escritor1.nome)
print(caneta1.marca)
maquina1.escrever()
escritor1.ferramenta = caneta1
escritor1.ferramenta.marca = "faber castell"
print(escritor1.ferramenta.marca)
print(caneta1.marca)
del escritor1
print(caneta1.marca)
maquina1.escrever()