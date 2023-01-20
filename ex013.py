salario = novo_salario = 0

nome = str(input("Nome do funcionário: ")).capitalize()
salario = float(input(f"Digite seu salário, {nome}: "))

novo_salario = salario + (salario * 15 / 100)

print(f'Antigo salário: R${salario:.2f} \nNovo salário: R${novo_salario:.2f}')

