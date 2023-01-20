#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de]
# trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente
#  de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
#  acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

ano_atual = datetime.today().year
cadastro_trabalhador = {"nome": str(input("Nome: ")),
                        "sexo": str(input("Sexo: [M/F] ")).strip().upper()[0],
                        "ano de nascimento": int(input("Ano de nascimento: ")),
                        "CTPS": int(input('Carteira de trabalho (0 não tem): '))}

cadastro_trabalhador["idade"] = (ano_atual - cadastro_trabalhador["ano de nascimento"])
if cadastro_trabalhador["CTPS"] != 0:
    cadastro_trabalhador["ano de contratação"] = int(input("Ano de contratação: "))
    cadastro_trabalhador["salário"] = float(input("Salário: R$"))
    if cadastro_trabalhador["sexo"] in "Mm":
        cadastro_trabalhador["ano de aposentadoria"] = cadastro_trabalhador["ano de contratação"] + 37
    elif cadastro_trabalhador["sexo"] in "Ff":
        cadastro_trabalhador["ano de aposentadoria"] = cadastro_trabalhador["ano de contratação"] + 32

print("-=" * 40)
for k, v in cadastro_trabalhador.items():
    print(f"{k} tem o valor de {v}" if k != "salário" else f"{k} tem o valor de R${v:.2f}")


