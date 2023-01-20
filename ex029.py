#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada
# Km acima do limite.

velocidade_carro = float(input("Qual a velocidade atual do carro? "))

if velocidade_carro > 80:
    multa = 7 * (velocidade_carro - 80) 
    print(f"\033[1;31mVocê foi multado!\nTaxa da multa: R${multa:.2f}\033[m")
else:
    print("\033[1;32mVocê está dirigindo com moderação!Continue assim e respeito as regras do trânsito!\033[m")