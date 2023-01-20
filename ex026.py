# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a
# letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a
#  última vez

frase = str(input("Digite um frase: ")).strip().upper()

print(f"A letra 'A' aparece {frase.count('A')} vezes em '{frase}'")
print(f'''A letra "A" aparece pela primeira vez na posição {frase.find("A")} 
E pela última vez na posição {frase.rfind('A')}''')