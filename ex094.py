# Crie um programa que leia nome, sexo e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os 
# dicionários em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

import time


inicio = time.time()
pessoa = dict()
galera = list()
resposta = ' '
cont = MediaIdade = 0

while True:
    cont += 1
    pessoa["nome"] = str(input('\033[1mNome: ')).strip().capitalize()
    pessoa["idade"] = int(input("Idade: "))
    MediaIdade += pessoa["idade"]
    while True:
        pessoa["sexo"] =    str(input("\033[1mSexo [M/F]: ")).strip().upper()[0]
        if pessoa["sexo"] in "MmFf":
            break
        print("\033[1;31mERRO!Por favor, digite somente \033[1;34mM\033[m ou \033[1;35mF\033[m")
    
    galera.append(pessoa.copy())
    while True:
        resposta = str(input("\033[1mContinuar [S/N]? ")).strip().upper()[0]
        if resposta in "SsNn":
            break
        print("\033[1;31mERRO!Por favor, digite somente 'S' ou 'N'\033[m")
    if resposta == "N":
        break
MediaIdade = (MediaIdade /cont)
print('-=' * 40)
print(galera)
print(f"A)\033[1;37mAo todo, foram cadastradas {cont} pessoas\033[m")
print(f"B)A média de idade é igual a {MediaIdade:5.2f} anos")
print("\nC)As mulheres cadastradas foram: ", end="")
for p in galera:
    if p["sexo"] == "F":
        print(f"{p['nome']}...", end='')
print(f"\n\033[1mD)Lista das pessoas acima da média: ")
for p in galera:
    for k,v in p.items():
        if p["idade"] > MediaIdade:
            print(f"\033[1m{k} = {v}\033[m  ", end='')
    print()

fim = time.time()
print(f"\033[1m<<< Programa finalizado com uma duração de {fim - inicio:.1f} segundos  >>>")