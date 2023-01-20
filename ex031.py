#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço
#da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens
# mais longa

custo_passagem = 0

distancia_viagem = float(input("Qual a distância da viagem? "))

if distancia_viagem <= 200:
    custo_passagem = distancia_viagem * 0.50

else:
    custo_passagem = distancia_viagem * 0.45

print(f"Fazendo uma viagem de {distancia_viagem}Km, a passagem custará R${custo_passagem:.2f}")