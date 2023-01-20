inverso = ''

frase = str(input("Digite uma frase: ")).strip().upper()
frase = frase.split(" ")
frase = "".join(frase)

'''for letra in range(len(frase) - 1, -1, -1):
    print(letra)
    inverso += frase[letra]

print(inverso)
if frase == inverso:
    print(f"{frase} É PALÍNDROMO")

else:
    print(f"{frase} NÃO é um palíndromo")'''

if frase == frase[::-1]:
    print(f"{frase} É um palíndromo")

else:
    print(f"{frase} NÃO É um palíndromo")