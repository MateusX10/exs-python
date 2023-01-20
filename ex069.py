#exercício Python 069: Crie um programa que leia a idade e o sexo de
#  várias pessoas. A cada pessoa cadastrada, o programa deverá
#  perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos. 


TotMaior18 = TotHomens = TotMulheresMenor20 = cont =  0

while True:
    cont += 1
    print(f"\033[1;32m================= {cont}º pessoa ================\033[m")
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]

    if idade > 18:
        TotMaior18 += 1

    if sexo in "Mm":
        TotHomens += 1

    if sexo in "Ff" and idade < 20:
        TotMulheresMenor20 += 1


    r = "A"
    while r not in "SsNn":
        r = str(input("Continuar [S/N]? ")).strip().upper()[0]
    
    if r == "N":
        break

print(f"Ao todo, {TotMaior18} pessoas são maiores de 18 anos,", end='')
print(f"{TotHomens} homens se cadastraram,", end='')
print(f"e {TotMulheresMenor20} mulheres têm menos de 20 anos")