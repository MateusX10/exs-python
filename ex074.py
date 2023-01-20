#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
#valor que estão na tupla.

from random import randint


tupla = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

for valor in tupla:
    print(valor)

print(f"O maior e o menor valor gerados na tupla foram: {max(tupla)} e {min(tupla)}")