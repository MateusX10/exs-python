#Faça um programa que calcule a soma entre todos os números que são múltiplos de três
#  e que se encontram no intervalo de 1 até 500.

cont = soma = 0

for n in range(3,501, 6):
    cont += 1
    soma += n


print(f'A soma de todos os {cont} números é {soma}')